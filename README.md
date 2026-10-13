# Herd Health Tracker

**PROG211 · Object-Oriented Programming 1**  
Limkokwing University of Creative Technology, Sierra Leone  
**Assignment:** Real-World Solutions under Digital Public Goods (DPG) Standards  
**Domain:** Agriculture · **Approved option:** Livestock Health & Tracking System

**Student:** Rashida Thomas · **Student ID:** 905005877 · **Lecturer:** Mr Alusine Lavalie
**GitHub repository:** https://github.com/thomasrashida798-cmyk/herd-health-tracker.git

> This is a beginner-level academic project. It is not a commercial livestock-management platform and has not been certified as a Digital Public Good. It records user-entered observations; it does not diagnose disease, prescribe treatment, or replace a veterinarian. All demonstration data is fictional.

---

## 1. Project overview

Herd Health Tracker is a menu-driven Python console application for recording health observations about individual livestock animals, reviewing each animal's history, and viewing its latest recorded health status. It demonstrates two interacting classes, a list of objects, reusable functions, and instance, class, and static methods.

The project is intentionally split into small modules so that data models, record-management logic, input validation, and console presentation have clear responsibilities. This organization improves readability and maintainability without introducing a database, external dependencies, or another primary storage structure.

## 2. Problem statement and objectives

Small livestock keepers may track animal health informally, making earlier observations difficult to retrieve. This program provides a simple way to keep each observation and review changes over time.

Objectives:

- Record observations for individual animals.
- Preserve every health record instead of overwriting history.
- Display all records, one animal's history, and its latest recorded status.
- Validate input and give clear messages when a value is invalid.
- Demonstrate the OOP concepts and data-structure requirements in the assignment brief.

## 3. Features

- Five-option console menu with keyboard-only navigation.
- Register an animal through its first health record.
- Reuse the same animal object when another record uses the same animal ID.
- Display all records in entry order and an animal's history oldest-date-first.
- Determine the current status by record date, not simply by entry order.
- Validate animal IDs, required text, age, date, status, and menu choice.
- Optional loading of three fictional demonstration records.
- Read-only tuple summary `(animal_id, current_health_status, record_count)` used by menu option 4. This is the optional tuple feature; its exact mark treatment depends on the official brief.

## 4. Technology and setup

- **Python:** 3.8 or newer is intended; the project uses only the Python standard library.
- **Runtime dependencies:** None.
- **Automated tests:** Python's built-in `unittest` framework.
- **Persistence:** None. The program keeps data in memory during one run; data is lost after exit.

No package installation is required.

## 5. Run the application

Open a terminal in the project root, then use either command:

```bash
python herd_health_tracker.py
```

or

```bash
python -m herd_health_tracker_app
```

At start-up, answer `y` to load the three fictional demonstration records or `n` to begin with an empty record list.

## 6. Run the automated tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

The test files are organized by concern:

- `tests/test_records.py` — record creation, display, animal history and out-of-order entries.
- `tests/test_validation.py` — age, date, status and required-field validation.
- `tests/test_objects.py` — object identity, storage, instance method, class method and static method.
- `tests/test_summary.py` — optional tuple summary.
- `tests/test_menu.py` — menu flows and clean exit.
- `tests/support.py` — shared scripted-input helpers and test setup.

The suite contains **30 automated tests**. In the current restructured build, all 30 passed during an independent run in the packaging environment. The retained original test log records the author's earlier test run; the current run log is saved at `evidence/logs/restructured_test_results.txt`. Passing tests do not prove the system is defect-free or guarantee an assignment mark.

## 7. Project structure and module responsibilities

```text
herd-health-tracker/
├── herd_health_tracker.py              # Simple root-level launcher / compatibility facade
├── herd_health_tracker_app/            # Application package
│   ├── __init__.py                     # Public interface and re-exports
│   ├── __main__.py                     # Enables: python -m herd_health_tracker_app
│   ├── constants.py                    # Approved statuses and age limit
│   ├── main.py                         # Application startup and menu loop
│   ├── models/                         # Domain objects
│   │   ├── __init__.py
│   │   ├── livestock_animal.py         # LivestockAnimal class
│   │   └── health_record.py             # HealthRecord class and methods
│   ├── services/                       # Record operations, separate from prompts
│   │   ├── __init__.py
│   │   ├── record_service.py            # Find, summarize, and add records
│   │   └── demo_data.py                 # Fictional sample records
│   ├── ui/                             # Console interaction and presentation
│   │   ├── __init__.py
│   │   ├── input_helpers.py             # Prompts and input collection
│   │   ├── record_entry.py              # Interactive add-record workflow
│   │   ├── record_display.py            # Record, history and latest-status views
│   │   └── menu.py                      # Menu display
│   └── utils/
│       ├── __init__.py
│       └── validation.py                # Date, age and status parsing
├── tests/                              # Automated test suite, grouped by concern
├── docs/                               # Architecture, tests and DPG notes
├── evidence/
│   └── logs/                           # Text logs from real program/test runs
├── screenshots/                        # Add genuine screenshot images here
├── report/
│   └── Herd_Health_Tracker_Report.docx # Assignment report
├── LICENSE
├── requirements.txt                    # Documents that no third-party packages are needed
├── .gitignore
└── CHANGELOG.md
```

### Layer responsibilities

| Layer | Responsibility | Examples |
|---|---|---|
| Models | Represent the main objects and their behaviour | `LivestockAnimal`, `HealthRecord` |
| Services | Perform data operations without asking for keyboard input | `add_record_to_list`, `find_animal`, `get_animal_summary` |
| UI | Ask questions and render console output | `add_health_record`, `display_health_records` |
| Utilities | Parse and validate small input values | `parse_date`, `parse_age`, `normalise_status` |
| Entry point | Create the one primary list and coordinate the application | `main()` |
| Tests | Verify expected behaviour using repeatable checks | `tests/` |
| Documentation and evidence | Explain the design and preserve verification material | `docs/`, `evidence/`, `report/`, `screenshots/` |

## 8. Class design

### `LivestockAnimal`

Represents one individual animal.

Attributes: `animal_id`, `species`, `breed`, `age_months`, `current_health_status`, `last_health_record_date`.

Instance method: `update_health_status(new_status, record_date)` updates the current status only when the incoming status is valid and its date is later than the stored date. The first record initializes the status and date. The method returns `True` when the current status changes and `False` when an older or same-day record is added.

### `HealthRecord`

Represents one health observation.

Attributes: `record_id`, `animal`, `date_checked`, `observed_signs`, `health_status`, `notes`. The `animal` attribute references a `LivestockAnimal` object, not a copied ID string.

- **Class method:** `get_total_records()` returns how many `HealthRecord` objects have been created during the current program run. It is not permanent storage.
- **Static method:** `is_valid_health_status(status)` validates one of the three approved status values.

Approved statuses are `Healthy`, `Needs Monitoring`, and `Veterinary Attention Required`. These are user-selected recordkeeping categories, not automated medical diagnoses.

## 9. Primary storage and record flow

`main()` creates one primary Python list named `health_records`, containing `HealthRecord` objects. There is no separate primary list or dictionary of animals.

When a record is added, the service searches this list for the animal ID. It reuses the matching animal object when found; otherwise it creates one. It then creates a health record pointing to that object, appends the new record to `health_records`, and updates current status only if the record date is later.

Historical records retain their original status. Temporary search results, comprehensions, and the on-demand tuple summary do not create a second persistent primary store.

Rules:

- Animal IDs are converted to uppercase (`an-001` and `AN-001` refer to the same animal).
- For an existing ID, the application reuses the species, breed, and age originally recorded.
- If two records have the same date, the first-entered record's status remains current because the update rule requires a strictly later date.
- Breed and notes are required text fields; enter `Unknown` or `None` when appropriate.
- Age must be a whole number from 0 to 1200 months. The upper bound is an author-chosen sanity limit, not an assignment requirement.
- Dates must be real calendar dates in `YYYY-MM-DD` format. Future dates are not rejected.

## 10. Fictional demonstration data

| Record | Animal | Species | Date | Observation | Status |
|---|---|---|---|---|---|
| HR-001 | AN-001 | Goat | 2026-10-01 | No abnormal signs reported | Healthy |
| HR-002 | AN-002 | Sheep | 2026-10-02 | Reduced appetite reported | Needs Monitoring |
| HR-003 | AN-001 | Goat | 2026-10-04 | Follow-up observation recorded | Veterinary Attention Required |

These examples are fictional. Breeds, ages, observations and notes are sample values, not real veterinary data.

## 11. Sample behaviour

For example, after adding an older record for `AN-001` with a date before `2026-10-04`, the application keeps that record in history but reports that the current status stays `Veterinary Attention Required`, based on the latest dated record.

Invalid age example:

```text
Invalid age. Please enter a whole number of months from 0 to 1200, such as 24.
```

Actual console sessions and test output are retained under `evidence/logs/`. They are text logs, not image screenshots.

## 12. Digital Public Goods alignment

This project applies DPG-style principles proportionately to a student assignment. It does **not** claim formal DPG certification.

- **Open-source readiness:** readable Python source, this README, an MIT licence, and no third-party dependencies.
- **Inclusivity and accessibility:** plain-language prompts, descriptive error messages, keyboard-only navigation, and labelled text output. Information is not communicated through colour alone.
- **Privacy:** fictional demonstration data only, no unnecessary personal information, and no network transmission. Records remain in memory and disappear on exit.
- **Modularity and reusability:** separate model, service, UI and utility layers; small reusable functions; and separation of record logic from interactive prompts.

Further discussion is available in `docs/dpg_alignment.md`.

## 13. Limitations

- Records exist only in memory and disappear when the program exits.
- The interface is console-only and English-only; it is intended for one user at a time.
- Records cannot be edited or deleted.
- The application does not diagnose, prescribe treatment, or generate veterinary alerts.
- The class-level record counter is for the current session only.
- Future dates are not rejected, and the age upper bound is an author-chosen sanity limit.
- The program has not been evaluated with real users or certified as a Digital Public Good.

## 14. Evidence and remaining submission tasks

Before submission, the student should:

1. Replace the student, student-ID and lecturer placeholders in this README and report.
2. Publish the repository and add the lecturer as a collaborator, as required by the brief.
3. Run the application and tests on the student's own machine.
4. Capture genuine screenshots showing the start/menu, adding and validating a record, all records, animal history/latest status, invalid input/exit, and the test run.
5. Insert the screenshots into the Word report and print the required hardcopy.
6. Recheck the final project against the exact lecturer-provided assignment brief.

The `screenshots/` folder includes instructions for collecting the missing image evidence. No fabricated screenshot images are included.

## 15. Development notes and licence

Use `docs/architecture.md` for the layer map and design rules, and `docs/testing.md` for the testing approach. See `CHANGELOG.md` for this structural reorganization.

Written for PROG211. Released under the MIT licence; see `LICENSE`. Update the author attribution before publishing.
