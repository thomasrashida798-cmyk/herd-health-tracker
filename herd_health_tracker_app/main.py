"""Application entry point and menu loop."""

from .services.demo_data import load_demo_data
from .ui import (
    add_health_record, display_animal_history, display_health_records,
    display_latest_status, display_menu,
)


def main():
    """Run the menu-driven application using one primary record list."""
    health_records = []  # The ONE primary list of HealthRecord objects.
    print("Herd Health Tracker")
    print("Records what you observe. It does not diagnose disease or replace a veterinarian.")
    print("Records are kept in memory only and disappear when you exit.")
    try:
        answer = input("Load 3 fictional demonstration records? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            load_demo_data(health_records)
            print("Fictional demonstration records loaded.")
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ").strip()
            if choice == "1":
                add_health_record(health_records)
            elif choice == "2":
                display_health_records(health_records)
            elif choice == "3":
                display_animal_history(health_records)
            elif choice == "4":
                display_latest_status(health_records)
            elif choice == "5":
                print("Goodbye. All records are cleared from memory when the program closes.")
                break
            else:
                print("Invalid choice. Please type a number from 1 to 5.")
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended. Exiting the program.")
