# Testing strategy

## Run the suite

From the project root:

```bash
python -m unittest discover -s tests -v
```

The suite uses the Python standard-library `unittest` framework and scripted input. It should not require a person to type answers while tests are running.

## Test module map

| Test module | Primary focus |
|---|---|
| `test_records.py` | Valid add, second record for one animal, display, history, latest status, older record entered later |
| `test_validation.py` | Age/date/status/required-field validation and unknown or empty lookup |
| `test_objects.py` | Object references and reuse, single primary list, historical statuses, instance/class/static methods |
| `test_summary.py` | Optional tuple summary and record count display |
| `test_menu.py` | Repeated menu, invalid menu choice, full sample session, add through menu, clean exit on EOF |

`support.py` contains shared test setup and scripted-input helpers. The class-level `HealthRecord` counter is reset before each test so the results are independent.

## Verification log

The 30 original test cases were retained and divided into focused files. In the current restructured build, the suite was executed in the packaging environment and all 30 passed. See `evidence/logs/restructured_test_results.txt` for the captured current run. The original author's Python 3.12.3 test log is retained separately in `evidence/logs/original_monolithic_version_test_results_python_3.12.3.txt`.

Passing this suite does not guarantee that no defect exists. Before submission, run it again on the student's own machine and capture the actual output for the report.

## Manual execution evidence still needed

Capture actual screenshots from the target computer showing:

1. Program start and menu.
2. Loading or beginning without fictional demo data.
3. Adding a record, including invalid input rejection.
4. Displaying all records.
5. Viewing a specific animal's history and latest status.
6. Handling an unknown ID, invalid menu choice and clean exit.
7. The automated test command with the final passing count.
