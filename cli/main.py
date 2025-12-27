from backend.services.entry_service import UserManager
from backend.services.query_service import QueryService
from backend.core.models import User
from backend.core.database import SessionLocal

def main_menu() -> str:
    print("\nRCCGSCK - Entry System")
    print("-" * 40)
    print("1. Add new entry")
    print("2. List all entries")
    print("3. Look up entry by ID")
    print("4. Delete all entries")
    print("5. Exit")
    print("-" * 40)
    return input("Enter choice: ").strip()

def confirm_user(user: User) -> bool:
    print("\nPlease confirm the information")
    print(f"First Name: {user.first_name}")
    print(f"Last Name: {user.last_name}")
    print(f"Phone: {user.phone}")
    print(f"Sex: {user.sex}")
    print(f"T-Shirt Size: {user.tshirt_size}")
    while True:
        choice = input("Is this correct? (Y/N): ").strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        print("Invalid input! Please enter yes or no.")

if __name__ == "__main__":
    # Create a single session for the CLI and inject it into services so
    # the CLI reuses one connection and closes it on exit.
    session = SessionLocal()
    um = UserManager()
    qs = QueryService()
    um.db = session
    qs.db = session

    try:
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
                    print(f"Entry saved successfully (ID: {user_id}).")
                else:
                    print("Entry discarded. Please re-enter the information.")

            elif choice == "2":
                all_entries = qs.get_all_entries()
                if not all_entries:
                    print("No entries found.")
                else:
                    print("\nAll saved entries:")
                    for entry in all_entries:
                        print(f"ID: {entry.id}")
                        print(f"First Name: {entry.first_name}")
                        print(f"Last Name: {entry.last_name}")
                        print(f"Phone: {entry.phone}")
                        print(f"Sex: {entry.sex}")
                        print(f"T-Shirt Size: {entry.tshirt_size}")
                        print("-" * 20)

            elif choice == "3":
                user_id_raw = input("Enter ID to search: ").strip()
                try:
                    user_id = int(user_id_raw)
                except ValueError:
                    print("Please enter a valid integer ID.")
                    continue
                entry = qs.get_entry_by_id(user_id)
                if not entry:
                    print("Entry not found.")
                else:
                    print(f"ID: {entry.id}")
                    print(f"First Name: {entry.first_name}")
                    print(f"Last Name: {entry.last_name}")
                    print(f"Phone: {entry.phone}")
                    print(f"Sex: {entry.sex}")
                    print(f"T-Shirt Size: {entry.tshirt_size}")

            elif choice == "4":
                confirm = input("Are you sure you want to delete all entries? (Y/N): ").strip().lower()
                if confirm in ["yes", "y"]:
                    um.delete_all_entries()
                else:
                    print("Deletion canceled.")

            elif choice == "5":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid input! Try again.")
    finally:
        session.close()
