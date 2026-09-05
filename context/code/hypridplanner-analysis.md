# The study planner as it stands on `main` of `hypridplanner`

A description of the code, written from the code, to check the thesis's claims against and to compare with Chapter 7.

Read on 2026-09-05 from `github.com/morischumacher/hypridplanner`, branch `main`, commit `c00ef4f` ("Initial commit", authored 2026-09-01). Nothing in this document comes from evaluation-study files or from the thesis; where the repository's own documentation makes a claim, the claim is marked as documentation and checked against the source where that is possible.

---

## 0. Provenance, and what this repository cannot tell us

**The repository has one commit and no history.** `git log` shows a single commit, `c00ef4f Initial commit`, dated 2026-09-01. There are no tags and no branches other than `main`. Three documents inside the repository refer to a tag `v1.0-evaluated` (README, `docs/thesis-map.md`, `docs/adr/0006`) and one to a branch `refactor/architecture` (`docs/deploying.md`). Neither exists here. So the question the thesis's rule asks second — *was this also true during the evaluation sessions?* — cannot be answered from git for any claim. It can only be answered from the repository's own documentation, which is testimony, and from Moritz.

**The repository's documentation and its author disagree about when this structure arrived.** Six architecture decision records in `docs/adr/`, all dated 2026-08-28, describe a refactor and give before-numbers for the code it replaced; `docs/architecture.md` says the refactor "happened after the system had been evaluated". Moritz states that the layered structure described here is the structure the tool had during the study, and that only features were added afterwards. Git cannot arbitrate, since there is one commit. This document takes the author's account as the working assumption: the structure below is the evaluated structure, and the per-feature questions of section 4 are the ones that remain. A reader of the repository will meet the ADRs' account first, which is worth knowing when the thesis is examined.

**Size.** 106,796 lines in the repository, of which about 62,000 are recorded test fixtures (`backend/tests/golden/*.json`) and 4,200 are `package-lock.json`. The application itself is roughly: backend `app/` ≈ 5,300 lines of Python over 45 files; frontend `src/` ≈ 17,500 lines over 90 files, of which the largest are `CurriculumGraphView.jsx` (2,124), `App.jsx` (1,336), `Sidebar.jsx` (1,102) and `dashboard/metrics.ts` (1,060); SQL migrations ≈ 3,400 lines, most of it seeded catalogue and course metadata.

**Dependencies, pinned from the lock files.** React 18.3.1, React Flow 11.11.4, Vite 5.4.20, TypeScript 7.0.2, Vitest 2.1.9, Playwright 1.62.1; Python 3.12 (Dockerfile), FastAPI, uvicorn, asyncpg, pydantic-settings (unpinned in `requirements.txt`); PostgreSQL 16 (`docker-compose.yml`, CI).

**Hosting.** The only hosting configuration in the repository is `frontend/vercel.json` (an SPA rewrite). Render and Neon appear in `docs/deploying.md` as the API and database hosts, with an operational procedure written around them; there is no `render.yaml` or Neon configuration. The API expects `DATABASE_URL` and `CORS_ORIGIN` from the environment.

---

## 1. Architecture

![Detailed architecture](figures/architecture.svg)

*Figure 1. The three tiers and every module in them. Browser: entry, feature hooks, presentational components, the framework-free domain layer, and one API client. Service: routers, use cases, repositories behind a unit of work, the rule engine over the curriculum documents, the recommender, infrastructure. Database: the normalised catalogue with its materialised view, the per-user tables, and the migration ledger. Arrows are dependencies; dashed arrows are reads of data rather than calls.*

Three tiers, three processes, two of them stateless.

The **browser** runs a single-page React application. `main.jsx` bootstraps the session (`GET /auth/me`), shows `AuthGate.jsx` when there is none, and otherwise renders `App.jsx` inside a `ProgramProvider`. `App.jsx` is an assembly file: it calls some thirty feature hooks in a deliberate order and passes their results to the components. State lives in the hooks; the plan itself lives in a pure reducer in `src/domain/plan/`. The browser talks to the service through `src/lib/api.js`, one `fetch` wrapper per endpoint, with `credentials: "include"` so the session cookie travels.

The **service** is a FastAPI application. A request enters a router in `app/api/`, which validates it with a Pydantic model, calls exactly one method on a service from `app/services/`, and returns what the service gives it. Services reach storage through a unit of work (`app/repositories/unit_of_work.py`) that hands them every repository bound to one connection (`read()`) or one transaction (`write()`). The rule engine (`app/rules/`) and the recommender (`app/recommendations/`) are pure Python with no I/O; both read the curriculum documents in `app/curriculum/`. Failures are raised as named domain errors (`app/domain/errors.py`) and turned into status codes by one table in `app/api/errors.py`.

The **database** is PostgreSQL. The catalogue is normalised (programme → exam subject → module → course) and projected into a materialised view that already holds the nested JSON the interface wants. Per-user data is five tables, the plan among them as one JSONB document per user.

---

## 2. The backend

### 2.1 Entry point and lifecycle

`app/main.py` builds the `FastAPI` object, installs CORS (origins from `CORS_ORIGIN`, defaulting to the local Vite ports), a request-logging middleware, and a handler that maps every `DomainError` to a JSON response. On startup, inside the lifespan, it applies outstanding migrations (`apply_pending`) before serving anything. Two meta endpoints exist: `GET /` and `GET /health`, the latter doing a database round trip.

`app/settings.py` reads `DATABASE_URL`, `CORS_ORIGIN`, `USE_CATALOG_MAT` and `MIGRATIONS_DIR` from the environment or a `.env` file.

### 2.2 The HTTP surface

| Route | Auth | Service call | Notes |
|---|---|---|---|
| `POST /auth/signup`, `/auth/signin` | none | `AuthService.sign_up / sign_in` | sets a `session_token` cookie and returns the token; passwords are `pbkdf2_sha256`, 200,000 iterations |
| `POST /auth/signout`, `GET /auth/me` | cookie or bearer | `sign_out / identify` | |
| `GET /catalog?program_code=` | required | `CatalogService.for_programme` (or all) | reads the materialised view, then overlays the user's term overrides |
| `GET /curriculum/prerequisites?program_code=` | required | `prerequisites.prerequisite_relations` | `{programCode, relations:[{source,target,kind}]}`; 400 for an unknown programme |
| `GET /planner-state`, `PUT /planner-state` | required | `PlannerService.load / save` | the whole plan document, `{state: {...}}` |
| `GET /profile-settings?program_code=` | required | `ProfileService.get` | start term, interests, career direction, toggles, locks, term overrides |
| `PUT /profile-settings/start-term` | required | `ProfileService.set_start_term` | 409 `ProgrammeLocked` / `StartTermLocked` |
| `PUT /profile-settings/course-terms` | required | `set_course_terms` | per-course winter/summer/both overrides |
| `PUT /profile-settings/recommendation-profile` | required | `set_recommendation_profile` | interests, career direction, toggles; 400 `SetupIncomplete` before a start term exists |
| `POST /rulecheck` | required | `RuleCheckService.evaluate` | see 2.5 |
| `POST /recommendations` | required | `RecommendationService.recommend` | see 2.7 |
| `POST /study-results` | **none** | `StudyResultsService.save` | writes the questionnaire payload as a JSON file under `backend/study_results/`, named by participant id and timestamp |

Authentication accepts either the `session_token` cookie or an `Authorization: Bearer` header; `current_user` tolerates anonymity, `require_user` does not. Sessions are rows in `auth_session` with an expiry.

The status table (`app/api/errors.py`) is short and is the only place status codes appear: `InvalidRequest`, `SetupIncomplete`, `UnsupportedProgramme` → 400; `NotAuthenticated` → 401; `ProgrammeNotFound` → 404; `UsernameTaken`, `ProgrammeLocked`, `StartTermLocked` → 409; `StorageFailure`, `RuleEvaluationFailed` → 500.

### 2.3 Services and repositories

Eight services, each one use case or a small family of them. Two are worth describing because they carry rules.

`ProfileService` holds the two locks. The programme is chosen once: a second, different programme raises `ProgrammeLocked`. The start term is fixed once, because it sets the winter/summer parity of every lane; a different one raises `StartTermLocked`, the same one is accepted silently. `set_start_term` takes a row lock on the user first so two first-time setups cannot race. Saving interests before a start term exists raises `SetupIncomplete` rather than creating a half-formed profile row. The profile row also carries the recommendation toggles, and two different default sets exist for them: `SETTINGS_TOGGLES` (five channels, what the settings screen shows) and `RECOMMENDER_TOGGLES` (the same plus `peer`, what the recommender runs).

`CatalogService` reads the catalogue and applies the user's term overrides on top of the seeded term availability before returning it, so a course the student has said runs in summer shows as summer everywhere.

`PlannerService` is two lines of logic: load the document, save the document. The repository stores `state` whole, replacing it on every save.

Repositories hold SQL and nothing else: `users`, `sessions`, `planner_state`, `catalog`, `profiles`, `course_term_overrides`. `CatalogRepository.candidates(program_code)` is the query the recommender draws its pool from (distinct courses of a programme with their attributes); it has an explicit `ORDER BY` so the pool order is total.

### 2.4 The curriculum as data

`app/curriculum/bachelor.json` and `master.json` hold each programme's regulations. Sets and tuples, which JSON cannot express, are written as `{"__set__": [...]}` and `{"__tuple__": [...]}` and restored on load; `load()` is cached for the process.

**Bachelor 033 521.** Constants: `TOTAL_ECTS` 180, `MIN_NARROW_ELECTIVE_MODULES` 7, `TRANSFERABLE_SKILLS_MIN/MAX_ECTS` 6 / 9, `BACHELORARBEIT_ECTS` 13, `MAX_ECTS_PER_SEMESTER` 42, `RECOMMENDED_ECTS_PER_SEMESTER` 30, `STEOP_POOL_MIN_ECTS` 8, `MAX_NON_STEOP_ECTS_BEFORE_STEOP` 22. Entries: `exam_subject_aliases` (13), `modules` (64), `course_to_module` (101 lookup keys — codes, titles and title variants, not 101 courses), `steop_mandatory_lv_keys` (10), `steop_mandatory_tags` (3), `steop_pool_keys` (23), `allowed_before_steop_extra` (15), `focuses` (7) with `focus_aliases` (21), `soft_prereqs` (2 pairs: EiP 1 → EiP 2, Software Engineering → Software Engineering Projekt), `split_variant_module_keys` (3), `recommended_prereqs` (36 entries).

**Master 066 937.** Constants: `TOTAL_ECTS` 120, `SUBJECT_MODULES_MIN_ECTS` 81, `TRANSFERABLE_SKILLS_MIN_ECTS` 4.5, `MAX_ECTS_PER_SEMESTER` 42, `RECOMMENDED_ECTS_PER_SEMESTER` 30. Entries: `exam_subjects` (17), `core_by_exam_subject` (6), `mandatory_modules` (3), `core_modules` (7), `variable_modules` (3), `advanced_topics_prefixes` (10), `prerequisites` (4 keys: the defence and the seminar each require the thesis, written once by name and once by code), `category_map` (35), `special_category_by_code` (16), `course_alias_to_name` (17), `recommended_prereqs` (21 entries).

Note the two per-semester limits are marked in both checkers as "not curriculum law: they are the plan-sanity limits the planner enforces", and the payload's own limits override them.

### 2.5 The compliance engine

![Compliance pipeline](figures/compliance.svg)

*Figure 2. `POST /rulecheck` from payload to result, with the two programmes' pipelines side by side in the order their checks run. Red boxes produce the message; the result shape is shared.*

`checker_for(program_code)` selects `rules/bachelor.py` or `rules/master.py` by the programme code with spaces removed. A missing code selects the master checker ("what the frontend relied on before it sent one"); an unknown code raises `UnsupportedProgramme` unless the caller passes `strict=False`, which the recommender does. `RuleCheckService` wraps the whole evaluation so that anything a checker raises becomes `RuleEvaluationFailed` (500).

Both checkers read the curriculum document in their constructor and expose the constants as class attributes. Both return one shape, `RuleCheckResult`: `ok` and `message` answer whether *the change just made* is allowed; `stats` carries the numbers the dashboard prints, and inside it `warnings[]` and `errors[]`; `missing[]` lists what the degree still needs. `ok = false` is what the frontend rolls back on; warnings and missing entries never block.

**Bachelor (973 lines).** `evaluate` runs, in this order: a wrong-programme guard; the load limits from the payload; `_collect_plan_totals` (accent-folds titles, maps each course to a module and a canonical category, parses ECTS and reports an unparseable value as a warning while dropping the course from every later pass); `_check_semester_load` (above the ceiling → error, above the recommended load → warning, below it → a "missing" note); `_check_variant_mixing` (a VU and a VO+UE of the same module together → error); two StEOP snapshots, one over done courses to decide whether the gate is open and one over done-plus-planned for progress, with `_steop_missing` feeding the missing list; `_check_pre_steop_courses` (more than 22 ECTS of non-StEOP work before the gate opens → error) and `_check_thesis_gating` (→ error); `_recommended_sequencing_warnings` over the two soft pairs (→ warning); the transferable-skills cap; `_collect_missing_requirements` (narrow electives, totals); the focus area, resolved through 21 aliases, which contributes stats and missing entries and only becomes an error if the payload sets `validateFocusAsStrict`; and `_build_dashboard`. The rejection message is the first error prefixed with the change: `rejected: cannot apply change (<type>) for '<courseCode>': …`.

**Master (753 lines).** `evaluate` parses lanes and courses (a parse error returns `ok=false` with no stats), builds the dashboard first (subject modules ≥ 81 ECTS, transferable skills ≥ 4.5, 120 total, core sets per subject), then checks duplicates, semester load, module consistency, the four hard prerequisite pairs (each a violation), recommended sequencing (warnings), and the core-before-elective condition per exam subject, which is deliberately "missing + warning, not a violation". `_make_actionable_message` names the action and, where the change carries it, the course code and semester: `Rejected plan_updated 'CODE' (semester 3): …`, `Rejected course_status_toggled 'CODE' (semester 2): …`.

What the two checkers share is stated in `rules/payload.py` and its docstring: the wire format, the result shape, the entry point, the shape of a rule set, and the reading of the credit limits — "there is very little of this, and that is the finding".

### 2.6 Prerequisite relations, for the graph

![Prerequisite relations](figures/prerequisites.svg)

*Figure 3. Three kinds of relation, one source, two consumers. The engine enforces or warns; the graph draws two kinds on one switch and reveals the third per node.*

`services/prerequisites.py` reads the same curriculum documents the checkers read and shapes them into `{source, target, kind}` pairs, so the engine and the graph cannot disagree. Three kinds: **soft** (the bachelor's two advisory pairs; planning the target first produces a warning), **hard** (the master's thesis-before-defence and thesis-before-seminar; planning the target first is rejected), and **recommended** — the curriculum's own *Erwartete Vorkenntnisse*, one entry per module naming the modules that teach what it expects, 36 entries in the bachelor and 21 in the master. The module docstring is explicit that the recommended kind "carries no consequence in the compliance engine and must not acquire one". The endpoint returns an empty list for a programme that encodes none, "which is a real answer rather than a missing one".

### 2.7 Recommendations

![Recommender](figures/recommender.svg)

*Figure 4. From the request to the list: context, six channels asked in a fixed order, one entry per course, a sort, and a trial placement against the rule engine.*

`RecommendationService.recommend` reads the profile (interests, career direction, toggles) and the candidate pool, builds a `Recommender` with the programme's checker, and evaluates. `build_context` lower-cases the interests, derives planned/done/parked code sets, and defines the candidates as the pool minus everything already planned, done or parked.

**Six channels**, each a class with a `name` (also its toggle key) and one method `suggest(plan, candidate)` yielding `Suggestion(score, evidence)`. They are composed in `engine.CHANNELS` in this order, and the order decides ties: the engine iterates candidates outer and channels inner, a course is recommended once, and the first channel to claim it supplies the reason.

1. **interest** — an interest matches a course three ways, weighted 1.5 (a listed topic), 0.8 (anywhere in the description), 0.4 (half the interest's words among the course's keywords); summed and divided by the number of interests named; clamped to 0.4–1.0. Evidence: `Matches your interests: focuses on <up to three matched topics>` or `covers topics related to …`. Silent when the profile names no interests.
2. **similarity** — reads the curated `similar_courses` links of every course the student has taken or planned, backwards; a link naming the candidate yields a fixed 0.85 with `similar to <taken course> (<curated evidence>)`.
3. **sequence** — the curriculum's own ordering (bachelor `soft_prereqs`, master `prerequisites`), resolved to catalogue codes by accent-folded name; 0.9 when a planned course needs the candidate first (`the curriculum expects this before planned course X`), 0.8 when the candidate follows a completed one.
4. **completed** — over the synthetic cohort, the share of students who finished a done course and also took the candidate; only shares of 50 % or more count; the share is the score and the evidence: `<n>% of students who completed <done> also took this`.
5. **internship** — the career direction's words against course skills (×2) and description, divided by the number of words, clamped 0.4–0.9; `develops skills for <direction> (<matched>)`. Silent without a career direction.
6. **peer** — the ten synthetic students whose choices most overlap the plan, weighted by overlap; score 0.4 + 0.5 × share, with the percentage in the evidence; when nothing overlaps (an empty plan) it falls back to raw popularity over the cohort and flags `cold_start`.

The **cohort** (`peer.py`) is synthetic: 50 students built from 5 tracks of 15 courses each, seeded from the md5 of the programme code so the same cohort comes back on every run, memoised per programme with an LRU bound of four entries. `completed` and `peer` both draw on it. There is no knowledge-graph module on `main`; `docs/architecture.md` still describes one, `docs/known-defects.md` records its removal.

**Assembly** keeps at most one record per course code and also suppresses a course whose *base name* (title with format and subtitle stripped, so "Analysis (VO)" and "Analysis (UE)" are one course) is already recommended or already in the plan. A record carries `id`, `courseCode`, `courseName`, `type` (the channel), `score`, `evidence`, `ects`, `category`, `examSubject`, `courseType`. Records are sorted by score.

**Rule filter** (`rules.py`). The plan is evaluated once as a baseline. Each of the top 100 records is then tried against the checker as if added: in a late trial lane (99) and in the earliest lane the plan uses, for every catalogue row that carries the code; it survives if any trial introduces no error and no warning beyond the baseline. A checker that raises on a candidate drops it; a checker that raises on the baseline stands the filter down and returns the unfiltered list. The result is cut at 15.

**Toggles.** The recommender honours six keys; a key not mentioned is on. The profile's settings screen stores five (no `peer`). The panel in the browser offers four chips (see 3.9). So a student can switch `sequence` and `completed` off only through the profile modal, and can never switch `peer` off from there.

### 2.8 Persistence, profile and study results

The plan is one JSONB document per user in `planner_state.state`, rewritten whole on every save; the frontend owns its shape (3.13). The profile is one row per (user, programme) in `user_program_profile`; per-course term overrides are rows in `user_course_term_override`. `POST /study-results` writes each questionnaire payload to a file rather than the database, "so that a participant's data is a file the researcher can copy off the machine".

### 2.9 Database schema and migrations

![Data model](figures/datamodel.svg)

*Figure 5. The schema as the migrations create it. Green: the shared catalogue. Orange: per-user tables. The plan is one document per user; the profile is one row per user and programme.*

Eleven migrations in `backend/sql/`, named `YYYYMMDDHHMM_slug.sql`: schema (2026-02-09), master catalogue, bachelor catalogue, the materialised view, auth and planner state (2026-02-12), term availability and profile (2026-02-25), master and bachelor term flags, recommendation profile (2026-05-18), course metadata, course similarities. `_ledger.psql` creates `migration_history` and remaps the earlier sequential filenames; it is not matched by the migration scan. `infrastructure/migrations.py` applies outstanding files in lexical order, records a checksum for each, and raises `MigrationDrift` if an applied file no longer matches disk. There are no down-migrations.

The seeded catalogue holds **84 course rows and 70 module statements for the bachelor programme, 105 course rows and 100 modules for the master** (counted from the seed files). The bachelor's `study_program` row records 180 ECTS over 6 semesters, the master's 120 over 4. Course metadata (`content` arrays used for interest and internship matching) and `similar_courses` (curated links with an English evidence sentence) are JSONB attributes on `course`.

### 2.10 Tests

`backend/tests/` holds 235 tests by the README's count; by file: a golden master over the rule engine (**38 recorded scenarios** in `fixtures.json`, compared field by field, plus determinism, non-mutation and non-degeneracy tests), a golden master over the recommender (**85 scenarios** in `recommender_fixtures.json`, plus a test that every channel is exercised), a contract test pinning every endpoint's status code and response shape (`response_shapes.json`), curriculum-document tests (including the pinned defect that six bachelor courses map to an undefined module), migration tests, rule tests (thresholds, invalid ECTS, StEOP wording), recommendation tests (cohorts, real catalogue, rule filter, strategies, trial placement) and a prerequisites-service test. CI runs `pytest` against a seeded PostgreSQL service.

---

## 3. The frontend

### 3.1 Entry and the auth gate

`main.jsx` asks `GET /auth/me`; while waiting it shows "Loading...". Without a session it renders `AuthGate.jsx`, which offers sign-in and sign-up. Sign-up collects a username and password and, on the same screen, the programme, the focus area (bachelor only), and a checkbox labelled **"Disable Graph View (User Study Persona 1)"** — the evaluation study's condition switch, still present on `main` (`AuthGate.jsx:105`, and again in `ProfileModal.tsx:178`). The chosen programme and the flag are handed to `App` on entry, and a first sign-up opens the setup modal.

`ProgramContext.jsx` holds the programme options (`033 521` Bachelor Informatics, `066 937` Master Software Engineering) and the current programme; `DEFAULT_PROGRAM_CODE` is the master.

### 3.2 The domain layer

`src/domain/` is framework-free: no React, no DOM, no network, tested by calling it.

**`plan/state.ts`** defines the state. `PlannerState` = `{programCode, byProgramme: Record<code, ProgrammePlan>, lastChange, changeCounter}`. A `ProgrammePlan` = `coursesBySemester` (one-based semester number → `PlanCourse[]`), `doneCourseCodes`, `parkedCourseCodes`, `courseMetaByCode` (notes, estimated hours as typed, grade 1–5), `semesterNotes`, `selectedFocus`, `loadLimits` (max/recommended ECTS 42/30, max/recommended week-hours 50/40), `graphView` (collapsed ids, node positions, filters, `filtersConfigured`, horizontal offsets). A `PlanCourse` carries `id, code, name, type, ects, category, examSubject, position, laneIndex, subjectColor, module`. A plan is kept per programme so a master plan survives a detour into the bachelor curriculum.

**`plan/reducer.ts`** is `(state, action) → state`, with no clock, randomness or I/O. Actions (`actions.ts`): `programme/selected`, `plan/replacedFromNodes`, `course/doneChanged`, `courses/doneChanged`, `course/metaChanged`, `semester/noteChanged`, `focus/selected`, `focus/selectedForProgramme`, `loadLimits/changed`, `graphView/changed`, `plan/imported`, `plan/cleared`. Every recorded change gets `id = changeCounter + 1`; a change is one of `plan_updated` (a diff of added, moved, removed), `course_status_toggled`, `focus_updated`, `semester_load_limits_updated`. An action may carry `meta.silent`, in which case no change is recorded — this is how a rollback avoids triggering the check that would roll it back again. Unchanged parts keep their identity so the view can compare by reference.

**`plan/nodes-to-plan.ts`** derives a course's semester from its node's `position.x` and its order from `position.y`: the canvas and the plan are two representations of one thing. **`plan/diff.ts`** produces the `plan_updated` change with the node ids the rollback later searches for. **`plan/snapshot.ts`** turns the stored document into state and back.

**`filters.ts`** is the graph filter engine over six dimensions: `obligationTypes` (mandatory / core / elective / elective_narrow / elective_broad), `ectsRange`, `courseTypes`, `examSubjects`, `progressStates` (todo / in_plan / done), `termAvailabilities`. Within a dimension values are disjunctive; across dimensions conjunctive. An empty selection means no constraint; a node with no metadata stays visible; a matching course keeps its ancestry visible; a collapsed subject or module is judged by its descendants.

**`terms.ts`** and **`layout.ts`**: lane parity from the start term (a winter-only course fits every second lane), `firstAllowedLaneAtOrAfter`, and the table geometry — `LANE_WIDTH` 360, `LANE_GAP` 20, `CARD_WIDTH` 270, `NODE_HEIGHT` 124, `GRID_SIZE` 16 (the snap grid), `COLLISION_GAP` 8.

**`nodes.ts`** builds the board's nodes and carries `VerticalSemantics = no_meaning | alphabetical | ects | custom`: the vertical order a lane's cards take, applied by the layout-semantics pill.

**`prefill/`**: `buildBachelorPrefillPlan(focus)` sequences most of the bachelor degree by focus area; `buildMasterPrefillPlan` places what the master prescribes; `course-variants.ts` resolves split modules (VU vs VO+UE) to one chosen variant. Both report the aliases they could not find.

### 3.3 Feature hooks and the assembly order

`App.jsx` calls the hooks in an order its header comment calls "the whole of what this file decides": the canvas is built before anything reads it, the rollbacks exist before the rule check that may call them, and the rebuild from a stored plan comes last. The features:

- **planner-board/** — `useBoardHydration` (rebuilds nodes from a stored plan on load and programme switch), `useBoardNodes`, `useBoardDragHandlers` (drop, drag, snapping, module-group drags), `useCoursePlacement` (add a course or module to a lane or the parking stage; the file's header explains why some placements write the plan through at once and drags commit on the next render — "the single most delicate thing in the codebase"), `usePlacementRules` (which lanes a course may take; every menu offers the Parking Stage first), `useTermAutoShift` (relocates stranded courses when the start season or a term override changes, forward first), `useBoardSemesters` (the lanes the plan needs, plus "+" lanes beyond the active count), `useCatalogueActions`, `useCourseCardActions`, `useCourseNodeData`, `useNodeStatusSync`, `LayoutSemanticsPill`.
- **rule-check/** — `useRuleCheckSync`, `useRuleCheckRollbacks`, `useRuleCheckFeedback` (sticky violation, milestones, transient success), `useRuleCheckState`.
- **recommendations/** — `useRecommendationRequests`, `useRecommendationList` (also a `recommendedCourseMap` that is plumbed into node data but rendered nowhere; the card's recommendation patch is commented out "per user request (RP only)").
- **dashboard/**, **profile/**, **catalogue/**, **prefill/**, **tour/**, and **app/persistence/**.

### 3.4 How an edit travels

![Edit flow](figures/edit-flow.svg)

*Figure 6. One plan change and its three consequences. The rule check and the recommendations request go out immediately; the save waits 500 ms. Each answer is acted on only while its change is still the newest.*

A drop or a button dispatches an action; the reducer records `lastChange`. Three effects watch it. `useRuleCheckSync` posts the planned and done courses, the change, the focus (bachelor only) and the load limits to `/rulecheck` **on every change, without debounce**; it remembers the change id per programme and ignores any answer whose id is no longer the newest. On `ok: false` it raises a red sticky banner for 5 seconds with the engine's message and calls the rollback matching the change kind — added courses removed, moved courses put back, a status toggle reversed — each dispatched with `meta.silent`. `useRecommendationRequests` posts to `/recommendations` on every change with the same staleness guard. `usePlannerPersistence` saves the whole document after 500 ms of quiet, and only if the initial load succeeded, so a failed load can never overwrite a real plan with an empty one; sign-out flushes the pending save.

Two further requests exist for a student who has only opened the planner: an `initial_sync` rule check that fills the dashboard, and an initial recommendations request, one per programme.

### 3.5 The Table View

The board is a React Flow canvas (`PlannerBoard.tsx`) on which lanes are columns 360 px wide with a 20 px gap; lane 0 is the **Parking Stage**, lanes 1… are semesters. A card's lane is its `position.x`; its vertical position is snapped to a 16 px grid on drop and collisions are resolved downward (`COLLISION_GAP` 8). Lanes are labelled by the start term's parity; a course taught only in one season may only be dropped on lanes of that season, and a drop elsewhere is refused before the engine is asked. `+` lanes beyond the active count appear in the pickers and open a new lane when used (`isPlus`).

The **Semester Picker** (`usePlacementRules`, rendered inside `CourseCard`) lists the Parking Stage first, then the semesters the course's term allows, then the plus lanes, revealed progressively (`plusRevealCount`). The card's action buttons depend on status: *Add to plan* for todo and parked, *Mark done / Unmark* for in-plan and done, *Remove from plan* for in-plan, done and parked, and *Move* which opens the same picker (see Figure 7 in 3.7).

The **lane header** shows the title and the planned ECTS total; a popover adds estimated hours per week (summed from the cards' typed values), the ECTS-weighted grade of done courses, the course notes in the lane, and a free-text lane note (`LaneColumn.jsx`). Load warnings come from the engine's stats, not from the header.

**Module backgrounds** (`ModuleGroupBackground.jsx`) draw a tinted panel behind a multi-course module's cards only while the group or one of its cards is hovered (`isVisible = isSelfHovered || isHoveredFromCard`), communicated through DOM events; a whole group can be dragged, in which case its children shift by the snap delta.

The **layout-semantics pill** at the bottom lets the student declare what the vertical order means: no meaning, alphabetical, ECTS, or a custom text; the alphabetical and ECTS choices re-sort each lane (`nodes.ts`). The graph has the same pill for its horizontal axis (`hierarchy` or custom) and vertical axis.

### 3.6 The Graph View

`CurriculumGraphView.jsx` builds a tree from the catalogue (programme → exam subject → module → course; a module with exactly one course is drawn as `courseDirect` at the module's depth) and lays it out itself: a fixed x per level (`X_BY_LEVEL`: root 40, subject 340, module/direct course 660, course 980) and a running leaf index for y, with collision resolution. There is no external layout library.

Every subject and module node is collapsible; collapsed ids persist in the plan's `graphView`. Two presets, **Expand** and **Collapse** (`hierarchyMode` `force_expanded` / `force_collapsed`), sit above a `normal` mode; interacting with a filter or a node returns to `normal` and to the ids collapsed before the preset. Filters live in a sidebar panel of six dimensions (3.2); expanding a node whose children the filters would hide relaxes those filters for that subtree (`relaxFiltersForExpandedSubtree`, up to three passes), and changing a filter never resets collapse. Filters and `filtersConfigured` persist. A node can be dragged **horizontally only**; the offset persists per node (`nodeXById`), and a moved parent carries its children's offset.

**Course relations** (Figure 3): a checkbox *Show prerequisites (n)* draws the soft and hard relations together — dashed amber "recommended before", solid red "required before" — only between nodes currently on the canvas; it is disabled with the text "(none in this curriculum)" when n = 0. Separately, a node that is an endpoint of *expected knowledge* relations carries a `⇠n` button that reveals that node's relations alone, dotted indigo, one node at a time; the sidebar names which node is revealed and offers *Hide*.

The graph's nodes are `GraphSubjectNode`, `GraphModuleNode`, `GraphCourseNode` (with the same border-weight encoding and status visuals as a card, plus the reveal button). `VisualLegend.jsx` is a toggleable panel explaining border weights, states, structure and the icons.

### 3.7 The course card and its encodings

![Lifecycle](figures/lifecycle.svg)

*Figure 7. The four statuses a course can have on `main`, the controls that move it between them, and what the card looks like in each.*

`utils/courseVisuals.js` defines the visual language and every surface uses it — card, graph node, catalogue row, recommendation card.

**Obligation** is drawn as a **border of three weights** in the exam subject's colour: thick for *mandatory*, medium for *core* (labelled "Enge Wahl (+)" in the bachelor, "Core (+)" in the master), thin for *elective* ("Breite Wahl (*)" / "Elective (*)") and for anything unclassified ("Other"). It is implemented as one, two or three stacked 1-px inset box-shadows (`layeredTypeShadow`, 5 px, 3 px and 1 px deep), which at screen size render as a single border of the corresponding thickness — the variable is named `layers` and the legend calls it `borderLayers`, but what the student sees is weight.

**Status** (`stateVisualByStatus`): *todo* white; *parked* white with a shadow; *in_plan* light grey fill; *done* light grey fill, grey border, grey text, opacity 0.8. The card's footer prints, left to right, the ECTS, the obligation label, and the status word in lower case: `done`, `planned`, `parked`, `not planned`.

**Term** is an emoji in the header: ☀️ summer, ❄️ winter, ☀️❄️ both, with a title "Available in …". The header also carries the short code and the teaching format.

**The popover** (info icon) edits notes, estimated hours per week, and the grade, the grade being editable only for a done course.

### 3.8 The catalogue sidebar

`Sidebar.jsx` lists the whole curriculum grouped by exam subject, then module, then course, each collapsible, with a search field ("Search courses/modules...") over module name, code and category and course name and code. Courses and whole modules are drag sources; each row also carries the *Add to plan* menu (the same picker) and a done toggle. A split module offers its variants. Status visuals match the cards.

### 3.9 The Recommendation Panel

`RecommendationPanel.jsx` is a fixed-position drawer at the left, beside the catalogue (`position: fixed; left: 0; zIndex: 1000`), toggled by a *★ Show Recs / Hide Recs* button in the toolbar; the board does not shift when it opens. It shows a title, the line "Smart suggestions based on your plan.", then **four toggle chips**: *Interests*, *Similarity*, *Internships*, *Other students* (keys `interest`, `similarity`, `internship`, `peer`). Toggling a chip saves the profile's `recommendation_toggles` and refetches. A recommendation whose `type` is switched off is hidden client-side as well.

Each card carries a **badge with an icon and a label per family** (`REC_TYPE_META`): ★ Interest match, → Sequence dependency, ≈ Content similarity, ✓ Based on completed, ▶ Internship lens, 👤 Other students — six, including the two that have no chip. The card shows the header line (code, format, term), the title, the evidence sentence truncated at 120 characters with a *show more* control, the ECTS and obligation label, and the same status-dependent actions as a course card; it is draggable onto a lane when its status is todo or parked, and clicking opens the picker. An expanded card repeats the evidence under "Why this suggestion?".

When the visible list is empty the panel shows 🎯 and either "All disabled" (every toggle off) or "No recommendations". There are no per-family tabs and no per-family explanation of an empty state.

### 3.10 The Dashboard

`PlannerDashboard.tsx` is the right panel. At the top: two KPI progress bars (planned+done and done against the target) and a mode switch, **Planning** and **Done**, each with its own section order and collapse state, persisted in the document. The target is `180` for the bachelor, hard-coded, and `ectsStats.target_total ?? 120` for the master (`metrics.ts:159`).

Sections are draggable into a student's own order (`useDashboardSectionOrdering`). Planning mode: `steop`, `focus`, `planned_category`, `planned_exam_subject`, `planned_semester`, `planned_hours`; Done mode: `steop`, `focus`, `category`, `exam_subject`, `done_semester`, `done_grade`; both: `missing` and `warnings` (`RequirementSections.tsx`). The StEOP and focus sections carry "Show StEOP rules" / "Show Focus Area info" disclosures and the requirement checklists. The semester sections show per-semester ECTS bars against the profile's limits, the hours section the typed estimates, the grade section the weighted grade. Everything numeric comes from the engine's `stats`; `metrics.ts` (1,060 lines) shapes it.

Banners: the compliance feedback strip at the top centre of the canvas (red for a refusal, blue "Checking rules...", green "accepted", grey otherwise); a **milestone** banner, green, fixed at the top, when the plan first crosses 25, 50, 75 or 100 % of the target (`Milestone reached: 50% completion (90.0/180.0 ECTS).`); and the prefill offers (3.12).

### 3.11 Profile and setup

`SignupSetupModal.tsx` runs on first entry: the programme, the focus area (bachelor), and the start term as season (Winter/Summer) and year. Saving it locks both on the server (2.3).

`ProfileModal.tsx` (reachable from the toolbar) shows the username; the **"Disable Graph View (User Study Persona 1)"** checkbox; the programme (read-only once locked) and focus area; *Interests (comma separated)*; *Career Direction / Internship Target*; a searchable list of the programme's courses with a winter/summer/both selector each (the term overrides); the five recommendation toggles; and the four load limits — max and recommended ECTS per semester, max and recommended week-hours per semester. `useProfileForm` (527 lines) is the form state; `useProfileSettings` loads and saves it and applies a changed start season through the term auto-shift.

### 3.12 Prefill, tour, legend

An empty plan triggers an offer (`PrefillNotifications.tsx`, top right): *Apply prebuilt plan* or *Keep current plan*; choosing a focus later offers the focus's plan. The onboarding tour (`OnboardingTour.jsx`) has seventeen steps — Explore the Curriculum, Shortlist Courses, Plan Semesters, Course Card Controls, Layout Semantics & Sorting, Recommendations (Show Panel), Evidenced Recommendations, Dashboard (Open Panel), Dashboard & Rulechecking, Profile Settings (Open Modal / Settings), Canvas Navigation, Switch to Graph View, What is this view for?, Graph Filters & Search, Align, Expand & Collapse, Repeat Anytime — remembered per student in `localStorage`. The legend is a panel toggled from the toolbar.

### 3.13 The stored document

`PersistSnapshot` = the planner state (every programme's plan, 3.2) plus two dashboard maps (section orders and open sections per mode, per programme) and the graph view state, saved as `planner_state.state`. A unit test (`legacy-document.test.ts`) reads a document "in exactly the form already stored for every participant", which is the repository's guarantee that older documents still load.

### 3.14 Tests and CI

`frontend/tests/unit/` (≈ 128 `it`/`test` calls in 9 files; the README says 112) covers the reducer, the filter engine, the prerequisite edge builder, the legacy document and hooks. `frontend/tests/e2e/` holds **21 Playwright tests** in four specs — the README and CONTRIBUTING say 17, which predates `graph-prerequisites.spec.js` (4 tests): the prebuilt plan, placing a course, term refusal, the parking stage, persistence, the dashboard, moving a course, the engine's refusal being undone "and says why", marking done, removal, dashboard state surviving a reload, a save carrying the programmes not on screen, the prerequisite switch and the per-node reveal, and a smoke test. CI (`.github/workflows/ci.yml`) runs `pytest` against a seeded database, `npm run typecheck`, `npm test`, `npm run build`, and the e2e suite with its own Chromium.

---

## 4. The code check, chapter by chapter

Verdicts: **holds** (the code does what the sentence says), **differs** (the code does something else; what it does is stated), **not on main** (the claimed change is absent), **cannot be settled here** (needs history or the live system). Chapters 7 to 9 are checked separately; this section covers 1 to 6.

Every verdict below is the state after the corrections of 2026-09-05 were settled with the author. Where a first reading of mine was wrong, the row says so rather than being quietly replaced, since the point of this document is to be checkable.

### 4.1 Chapter 1 — Introduction

Five claims about the tool. **All five hold.**

| Claim | Verdict | What the code shows |
|---|---|---|
| "unites a curriculum graph and a schedule-managing table over a single shared plan" | **holds** | One reducer; `coursesBySemester` is the single representation and both views are projections of it. A card's lane is its node's `position.x`. |
| "checks that plan against the regulations of two degree programmes in real time" | **holds** | `useRuleCheckSync` posts on every plan change with no debounce; only the save is debounced. Two rule sets, selected by programme code. |
| "embeds explainable recommendations within the planning workflow" | **holds of the artefact** | Six channels, each writing the sentence the student reads; cards are draggable into a lane. How many could fire during the sessions is a separate question. |
| the graph "renders no semester dimension against which that commitment could be judged" | **holds** | Four fixed columns by curriculum depth, subject bands vertically, horizontal-only dragging. No semester enters the layout. |
| "the constraints it does not model are silent rather than wrong" | **holds** | `internship`, `exchange` and every term word appear nowhere in `app/rules/`; `_check_semester_load` errors above the maximum, warns above the recommended load and only notes below it, with both thresholds from the profile rather than the task. |

### 4.2 Chapter 2 — Methodology

The scope boundaries are claims about what the artefact does not do. **All seven hold**, three with a nuance worth stating.

| Claim | Verdict | What the code shows |
|---|---|---|
| "desktop-scale single-page web application; use on small screens is not addressed" | **holds** | A React SPA behind an index rewrite. `global.css` contains no media query, and the layout is built from fixed pixel widths (lanes 360 px, panels at fixed offsets, `position: fixed`). Small screens are not addressed, exactly as claimed. |
| **OOS1**, no automated planning | **holds, two nuances** | The engine advises and blocks; nothing re-balances a plan. The prefill is a hand-written template per programme, not a computed plan, and the student accepts or declines it. Two things do write the plan without being asked: accepting that prefill, and `useTermAutoShift`, which relocates courses stranded by a change of start season or term override. Both are repairs or offers rather than planning on the student's behalf, but neither is mentioned where OOS1 is stated. |
| **OOS2**, programme-level granularity | **holds** | `deadline`, `calendar` and `appointment` appear nowhere in the application. The finest unit anywhere is a course in a semester. |
| **OOS3**, no live connection to the institutional systems | **holds** | No TISS, LMS, Moodle or scraping code; the catalogue is seeded by migration and served from a materialised view. |
| **OOS4**, no community features | **holds** | No rating, review, comment, upload or sharing code of any kind. |
| **OOS5**, recommendation quality is not a contribution; "standard techniques over synthetically generated prior-student histories" | **holds, one nuance** | The cohort in `peer.py` is synthetic and seeded from the programme code. But only two of the six channels read it (`peer`, `completed`); the other four read the student's own profile, the curated catalogue links and the curriculum's ordering. The sentence reads as though the whole recommender runs on synthetic data. |
| "every curriculum rule the system checks … belongs to one of these two programmes, and the Compliance Engine holds a separate rule set for each" | **holds** | `checker_for` selects `rules/bachelor.py` or `rules/master.py`; no third rule set exists, and an unrecognised code is refused unless the caller passes `strict=False`. |

### 4.3 Chapter 3 — Related Work

One claim about the tool this thesis builds, inside the gap statement.

| Claim | Verdict | What the code shows |
|---|---|---|
| the tool "unites a browsable curriculum graph, rendering programme structure together with the prerequisites the curriculum formally fixes, with a schedule-managing table over a single, synchronised plan" | **holds** | Containment as the default layout, prerequisites as a togglable overlay, one plan behind both views. |
| — but the phrase "the prerequisites the curriculum formally fixes" | **open question, not a code defect** | The switch draws two kinds together: the Master's `prerequisites` (enforced) and the Bachelor's `soft_prereqs` (advisory). Both live in `app/curriculum/*.json` and `services/prerequisites.py` reads them as curriculum data, while the thesis glossary defines a soft dependency as "curated for this tool rather than published by either curriculum". Either the glossary is wrong about the two Bachelor pairs, or the curriculum document mislabels curated pairs as published ones. This cannot be settled from the code; it needs the curriculum PDF and Moritz. |

Everything else in Chapter 3 is a claim about other people's systems and belongs to the citation audit, not here.

### 4.4 Chapter 4 — Formative Study

**Nothing to check.** The chapter is about the study and the non-functional Figma prototype. It makes no claim about the built tool.

### 4.5 Chapter 5 — From Themes to Requirements

The chapter's own prose holds, including the general sentence about the Delineations, which I first read as false and which survived checking (below).

| Claim | Verdict | What the code shows |
|---|---|---|
| 13 features carrying 55 numbered requirements | **holds** | Counted in the appendix. |
| FEATURE-005 Req. 3 (self-assessed readiness) "not carried into the implemented system" | **holds** | `readiness`, `strength` and `risk` appear nowhere in the application. |
| FEATURE-013 Reqs. 1, 3, 4 (named, cross-view groups) "not carried into the implemented system" | **holds** | No group is ever created, named or renamed by a student; `groupId` is always a curriculum module's identifier. |
| FEATURE-013 Req. 2 (positions persist) "was implemented" | **holds** | `PlanCourse.position` in the plan and `nodePosById` in the graph view, both stored. |
| **"Every other exclusion recorded in a Delineation follows from a scope boundary … or from a design decision stated there, not from what was built."** | **holds** | I first read this as false in four places. Three of the four are answered by the author and one by the appendix itself; the settlement is below. |

**The four I flagged, and why the sentence stands (settled 2026-09-05).**

- **FEATURE-002 Req. 3**, module-based progress. There is no module section in the Dashboard, and `metrics.ts` computes `moduleProgressForDashboard` without anything consuming it. Moritz's answer: most Bachelor modules hold a single course, so the category and exam-subject breakdowns already report at that granularity. The curriculum data agrees, 41 of the 52 Bachelor modules carry one lookup key. A design judgement rather than a silent shortfall; Chapter 7 records that the section does not exist.
- **FEATURE-002 Req. 5**, a projected completion semester. Nothing forecasts one. Moritz's answer: a projection is planning on the student's behalf, which OOS1 excludes. That makes it an exclusion following from a scope boundary, which is what the sentence claims. The thinnest of the four, since OOS1's text is about not planning rather than not forecasting.
- **FEATURE-005 Req. 2**, distribution of assessment types. **My finding was wrong.** FEATURE-005's own Delineation already excludes exam-load and exam-period collision detection under OOS3 and OOS2, and the distribution of assessment types is that same exam-clustering concern; the requirement's other two parts, total ECTS and threshold flags, are both implemented. Recorded in a Delineation, following from a scope boundary, exactly as the sentence says.
- **FEATURE-008 Req. 3**, alternatives when a course becomes unavailable. The Delineation excludes automated detection under OOS3, and the manual flag exists. Moritz's answer: the rest follows from how the tool works, since the rule check re-runs on the shift and the panel is where alternatives are found.

Two further requirements are met differently from how they are written, which is a documentation question rather than a shortfall:

- **FEATURE-007 Req. 4**, "users can enable/disable recommendation families individually", naming five. Four chips exist, in the panel (`interest`, `similarity`, `internship`, `peer`). `sequence` and `completed` have no control anywhere. The five-key `SETTINGS_TOGGLES` in `services/profile.py` is a backend default with no interface behind it; the profile screen holds interests and career direction and no switches at all. Chapter 6 now names the four the panel presents and asserts no total. Moritz's reading is that the sequence family is the graph's hard-dependency edges rather than a fifth chip, which is why the panel is not missing anything; how many families the thesis should claim in total is still open.
- **FEATURE-012 Req. 1**, "recommendations are displayed as annotations". The tool does the opposite on purpose: recommendations stay in the panel and nothing is drawn on the canvas or in the catalogue. Section 6.12.2 argues for it, and FEATURE-012's Delineation says "None beyond the overall scope boundaries", so the departure is stated in the thesis but not in the specification.

### 4.6 Chapter 6 — Design

| Claim | Verdict | What the code shows |
|---|---|---|
| Obligation encoded in **border weight**, three steps (§6.2.1) | **holds** | Thick, medium, thin in the subject colour, implemented as stacked inset shadows that render as one border of the given weight. |
| Four lifecycle states and the transitions of Figure 6.8 | **holds** | Including `planned → parked` through the picker. |
| Parked state distinguished by a label on the card | **holds** | Footer word "parked". |
| Course-card header: abbreviation, course type, term | **holds** | The term as ☀️ / ❄️ / ☀️❄️. |
| Six recommendation families; five toggle chips in Figure 6.12; four family symbols | **differs** | Six families, each rendering a badge that names it **in words**: `REC_TYPE_META` defines an icon per family and `renderRecommendationPatch` prints only the label, so no symbol is ever drawn. **Four** chips, in the panel only. `sequence` and `completed` have no control anywhere; the five-key `SETTINGS_TOGGLES` is a backend default with no interface behind it. The "Sequence" chip in Figure 6.12 does not exist. Corrected in Chapter 6. |
| Toggle preferences persist as part of the profile | **holds** | `recommendation_toggles`, written by the panel's chips. |
| Recommendations confined to the panel; nothing on the canvas or in the catalogue | **holds** | `renderRecommendationPatch` is imported by the card and the catalogue and called by neither; the card's call site is commented out. |
| An accepted card is removed from the panel | **holds** | Candidates exclude planned, done and parked codes on the next request. |
| Filtering: six dimensions, disjunctive within, conjunctive across; relax-on-expand; collapse survives filtering | **holds** | `filters.ts`, `relaxFiltersForExpandedSubtree`. |
| Three batch presets: Collapse all, Expand all, **Restore my layout** | **differs** | Two buttons, Expand and Collapse. The previous collapse set is restored implicitly at the next interaction; there is no third control. |
| Graph nodes draggable horizontally only, offsets persist | **holds** | `nodeXById`. |
| Lane header: label and ECTS, with hours, weighted grade and notes on demand | **holds** | `LaneColumn.jsx`. |
| **"two automatic sort modes … while allowing users to return to their manual arrangement afterwards"** (§6.6.2) | **differs** | Choosing alphabetical or ECTS **rewrites `position.y` for every card in the lane**. Returning to "no meaning" sorts by `position.y`, which is now the sorted order, so the manual arrangement is gone rather than restored. |
| Module backgrounds appear only on hover, click or drag | **holds** | Hover, self or child. |
| Setup dialog collects programme and start term | **holds** | It collects two more things the section does not name: the focus area, and the study's "Disable Graph View" switch. |
| **Profile: "Exceeding hard limits triggers prominent visual warnings in the Dashboard; exceeding soft limits triggers subtler warnings"** (§6.11) | **differs, in both directions** | For ECTS the hard limit does not warn, it **blocks**: the engine returns an error, the change is refused and rolled back. For weekly hours nothing happens at all — see below. |
| Dashboard: four levels Programme, Category, Semester, Module | **differs** | The sections are StEOP, focus, category, exam subject, semester, and hours or grade, plus missing and warnings. There is no module level. |
| Two Dashboard modes with independent order and collapse; milestones at 25/50/75/100 % | **holds** | |
| Transferable skills listed as an obligation category (§6.10) | **differs, but not as I first put it** | It *is* a category in the rule engine's own vocabulary and does appear in the Dashboard's breakdown, so the sentence is not wrong about the Dashboard. What is wrong is the enumeration: the Bachelor checker's categories are eight (mandatory, narrow elective, broad elective, free, transferable skills, thesis, and the two introductory-phase kinds), not four, and naming four contradicted the three-tier encoding of §6.1.5. It also carries a credit cap, Bachelor 6–9 and Master at least 4.5. Chapter 6 now names no buckets. |
| Compliance engine invoked after every action, returning status, per-category statistics, hard violations and soft warnings; messages name course, semester and action | **holds** | With a third output alongside errors and warnings: the `missing` list. |
| "A fully expanded 120-ECTS Master programme contains well over 100 nodes" | **holds** | 105 course rows, 100 modules, 17 exam subjects in the seeded Master catalogue. |

**One number carried forward, because it is not a Chapter 6 claim.** Chapter 7 (Section 7.8.2) and Chapter 9 both wrote "a graph of 101 courses" for the Bachelor programme. 101 is the number of lookup keys in `course_to_module`, which counts course codes, titles and title variants, so the same course is counted more than once; the seeded Bachelor catalogue has 84 course rows, and 68 of the 101 keys are code-like. **Corrected in both chapters, in the Section 0 register, and in the tool's own `prerequisites.py`, which repeated it.** What is left for the Chapter 7 to 9 pass is the rest of that Chapter 9 sentence: the two edges it counts are the Master programme's enforced pairs, since the Bachelor's two are advisory and the evaluated overlay drew only enforced ones.

**The weekly-hours limits are never enforced.** The client sends `maxWeekHoursPerSemester` and `recommendedWeekHoursPerSemester` on every rule check; `RuleCheckPayload` declares neither, so Pydantic drops them before the checker is called, and "week" and "hours" appear nowhere in `backend/`. The two values reach only the Dashboard's planned-hours section, which sums the estimates the student typed per course and colours one line against the *recommended* value; the *maximum* is used only to scale a bar. A student can set a hard weekly-hours ceiling that nothing checks. This is what makes §6.11 wrong in the second direction, and it is a third constraint the completion signal does not model, alongside the exchange semester and the band's lower bound. Settled 2026-09-05. The missing module level and the irreversible sort stand as design in Chapter 6 and are recorded nowhere else, since the section drafted for Chapter 7 was deleted; neither contradicts another chapter and no participant met either. This one was corrected, because §6.11 contradicted Chapter 8's own finding that the upper bound blocks and the lower bound is silent (E-P35). §6.11 now states the decision: the target advises, the maximum limits, and only credits are held to the limit, because the weekly hours are the student's own per-course estimate.

## 5. What Chapter 7 would keep, if this document were reduced to it

Section 1 is the chapter's opening figure and its System Overview, less the hosting caveat. Section 2.2 is the endpoint table, which the chapter does not have and would benefit from. Sections 2.3 to 2.5 are the Backend section, with Figure 2 replacing the prose walk through the pipeline. Section 2.6 is the material the chapter's edge-layer subsection needs, with the correction that there are three kinds of relation and two ways of drawing them. Section 2.7 is the Recommendation Support subsection, corrected for the knowledge graph's absence and the toggle counts. Section 2.9 is the Data Model with its figure. Section 2.10 and 3.14 are Verification. Sections 3.2 to 3.4 are the Frontend section with Figure 6 replacing the edit-flow figure. Sections 3.5 to 3.12 are what the chapter calls What a Student Sees, and are where the thesis's chapters 6 and 7 disagree with the code most; they are the sections to read first when correcting the design chapter.

What would be cut: the provenance discussion (section 0) is working material, as are the claim tables (section 4); neither goes into the thesis.
