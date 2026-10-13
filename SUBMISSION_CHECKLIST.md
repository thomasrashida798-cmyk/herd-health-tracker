# Final submission checklist

Use this checklist after the final code review. The boxes are not an automatic certification; each item needs to be checked against the actual submission.

## Source code and functionality

- [ ] The project runs using `python herd_health_tracker.py`.
- [ ] The project also runs using `python -m herd_health_tracker_app`.
- [ ] All automated tests pass using `python -m unittest discover -s tests -v`.
- [ ] The two classes, meaningful attributes, object relationships, primary list and required methods are present.
- [ ] The add-record and display-record functions work.
- [ ] Historical status is preserved and current status is based on record date.
- [ ] Invalid input and empty states are handled clearly.
- [ ] Optional tuple feature has been checked against the exact brief.

## Repository and documentation

- [ ] Replace `[Student Name]`, `[Student ID]`, and `[Lecturer Name]` where they appear.
- [ ] Add the correct GitHub repository URL to the report and README.
- [ ] Confirm the README matches the final source and test results.
- [ ] Review `docs/architecture.md`, `docs/testing.md`, and `docs/dpg_alignment.md`.
- [ ] Check for uncommitted/temporary files and exclude `__pycache__` folders.
- [ ] Confirm the MIT licence attribution is appropriate before public release.

## Evidence and submission

- [ ] Capture genuine screenshots on the student's computer.
- [ ] Include screenshots of program start/menu, record creation and validation, displaying all records, viewing history/latest status, invalid ID/menu handling, exit, and passing tests.
- [ ] Insert those screenshots into the Word report; do not leave the `[INSERT SCREENSHOT ...]` placeholders.
- [ ] Confirm the report uses Tahoma, 10 pt, 1.15 line spacing, and justified body paragraphs as required by the assignment brief.
- [ ] Publish the repository and add the lecturer as a collaborator, then verify access.
- [ ] Print the hardcopy and verify it includes actual execution screenshots.
- [ ] Recheck every requirement against the official assignment brief before submission.
