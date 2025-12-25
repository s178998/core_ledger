from backend.services.entry_service import UserManager
from backend.services.query_service import QueryService
from backend.core.models import User

def main_menu() -> str:
    print("\nCORE LEDGER - CLI")
    print("-" * 40)
    print("1. Add new entry")
    print("2. Exit")
    print("-" * 40)
    return input("Enter choice: ").strip()

def confirm_user(user: User) -> bool:
    print("\nPlease confirm user details:")
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
        else:
            print("Invalid input! Please enter Y/N.")

if __name__ == "__main__":
    um = UserManager()
    qs = QueryService()

    while True:
        choice = main_menu()
        if choice == "1":
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            phone = input("Phone: ").strip()
            sex = input("Sex (M/F): ").strip().upper()
            tshirt_size = input("T-Shirt Size (S/M/L/XL/XXL): ").strip().upper()

            user_id = um.create_user_with_confirmation(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "sex": sex,
                    "tshirt_size": tshirt_size,
                },
                confirm_user
            )
            if user_id:
                print("User saved successfully!")
            else:
                print("User discarded. Please try again.")
        elif choice == "2":
            print("Exiting CLI...")
            break
        else:
            print("Invalid choice! Try again.")
