"""Simple command-line interface for Core Ledger.

This module exposes a small interactive menu used to create and view
user entries. It intentionally avoids complex argument parsing to keep
the demo focused and easy to test.

Some features are commented out due to this being only phase one.
For future development, features will be uncomented for the implementation of other phases
"""

from services.entry_service import UserManager
from services.query_service import QueryService
from core.models import User


def main_menu() -> str:
    """Display the main menu and return the raw user choice string."""

    print("\nRCCGSCK - Entry System")
    print("-" * 40)
    print("1. Add new entry")
    # print("2. List all entries")
    # print("3. Look up entry")
    # print("4. Delete all entries")
    print("2. Exit")
    print("-" * 40)
    choice = input("Enter choice: ").strip()
    return choice


def confirm_user(user: "User") -> bool:
    """Ask the operator to confirm a User object's fields.

    Returns True when the operator confirms, False otherwise.
    """

    print("\nPlease confirm the information")
    print(f"First Name: {user.first_name}")
    print(f"Last Name: {user.last_name}")
    print(f"Phone: {user.phone}")
    print(f"Sex: {user.sex}")
    print(f"T-Shirt Size: {user.tshirt_size}")
    while True:
        choice = input("Is this correct? (Y/N): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        if choice in ["no", "n"]:
            return False
        else:
            print("Invalid input! please enter yes or no.")


if __name__ == "__main__":
    um = UserManager()
    qs = QueryService()

    while True:
        choice = main_menu()
        if choice == "1":
            first_name = input("Firstname: ").strip()
            last_name = input("Lastname: ").strip()
            phone = input("Phone number: ").strip()
            sex = input("Sex (M/F): ").strip().upper()
            tshirt_size = input("T-shirt size (S, M, L, XL, XXL): ").strip().upper()

            user_id = um.create_user_with_confirmation(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "sex": sex,
                    "tshirt_size": tshirt_size,
                },
                confirm_user,
            )
            if user_id:
                print("Entry saved successfully.")
            else:
                print("Entry discarded. Please re-enter the information.")
        # elif choice == "2":
        #     all_entries = qs.get_all_entries()
        #     if not all_entries:
        #         print("No entries found.")
        #     else:
        #         print("\nAll saved entries:")
        #         for entry in all_entries:
        #             print(f"First Name: {entry.first_name}")
        #             print(f"Last Name: {entry.last_name}")
        #             print(f"Phone: {entry.phone}")
        #             print(f"Sex: {entry.sex}")
        #             print(f"T-Shirt Size: {entry.tshirt_size}")

        # elif choice == "3":
        #     user_id_raw = input("Enter Id to search: ").strip()
        #     try:
        #         user_id = int(user_id_raw)
        #     except ValueError:
        #         print("Please enter a valid integer id.")
        #         continue
        #     entry = qs.get_entry_by_id(user_id)
        #     if not entry:
        #         print("Entry not found.")
        #         continue
        #     print(f"First Name: {entry.first_name}")
        #     print(f"Last Name: {entry.last_name}")
        #     print(f"Phone: {entry.phone}")
        #     print(f"Sex: {entry.sex}")
        #     print(f"T-Shirt Size: {entry.tshirt_size}")
        elif choice == "2":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input! Try again.")








