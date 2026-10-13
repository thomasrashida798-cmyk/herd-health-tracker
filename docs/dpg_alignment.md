# Digital Public Goods (DPG) alignment notes

This document explains proportionate design choices for the PROG211 assignment. It does not assert that the application has been evaluated or certified as a Digital Public Good.

## Open-source readiness

- The source is organized into readable Python modules.
- The repository includes setup/run instructions and test instructions.
- The project uses no third-party runtime dependencies.
- An MIT licence is included. The student should confirm the author attribution before publishing.

## Inclusivity and accessibility

- The interface is keyboard-operated and menu-driven.
- Prompts use plain language and explain invalid input.
- Output uses descriptive labels and does not depend on colour to communicate a status.
- The console and its labels are English-only; localization is outside the current scope.

## Privacy

- Demonstration records are fictional.
- The program does not request personal information, connect to a network, or write records to persistent storage.
- All program records are discarded when the process exits.
- The program is not suitable for safeguarding real operational records without additional design and review.

## Modularity and reusability

- `models/` contains the domain objects.
- `services/` implements non-interactive record operations.
- `ui/` handles prompts and display.
- `utils/` validates date, age and status input.
- Automated tests are separated by concern.

## Limits of these claims

These are project design features and explanations for the academic brief. They are not a formal DPG assessment, security audit, accessibility certification, or production-readiness claim.
