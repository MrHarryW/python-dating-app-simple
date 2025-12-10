from ui import loading_screen
from validation import ageCheck, passwordCheck, get_int
from profiles import create_basic_profile, collect_list, create_interests
from database import save_user, username_exists, validate_login
from logic import get_partners, random_date_day

def main():
    loading_screen()

    print("Welcome to Harry's Dating App\n")
    
    while True:
        age = get_int("Enter your age: ")
        if ageCheck(age):
            break
        print("You must be 18 or older.\n")

    print("\nAre you a new user or returning?")
    print("1. New User")
    print("2. Returning User")
    choice = input("> ")

    username = ""
    password = ""

    if choice == "1": 
        print("\n--- Account Creation ---")

        while True:
            username = input("Choose a username: ")
            if username_exists(username):
                print("That username is already taken. Try another.")
            else:
                break

        while True:
            password = input("Choose a password (8+ characters): ")
            if passwordCheck(password):
                break
            print("Password too short.\n")

        print("\nAccount created successfully!\n")

    else:
        print("\n--- Login ---")
        while True:
            username = input("Username: ")
            password = input("Password: ")

            user = validate_login(username, password)
            if user:
                print("\nLogin successful! Welcome back,", user["profile"]["name"])
                return  # If returning user, stop here OR load their profile
            else:
                print("Incorrect username or password. Try again.\n")

    print("\nLet's create your dating profile...\n")

    profile = create_basic_profile()
    profile["holidayDestinations"] = collect_list("Holiday destination: ", 3)
    profile["favouriteActivities"] = collect_list("Favourite activity: ", 3)
    profile["fiveThings"] = collect_list("Something you can't live without: ", 5)
    profile["interests"] = create_interests()

    save_user(username, password, profile)
    print("\nYour profile has been saved!\n")

    partners = get_partners(profile["interests"]["gender"])

    print("\nPossible matches:")
    for p in partners:
        print("-", p[0])

    chosen = input("\nChoose a partner: ")
    found = False
    for p in partners:
        if p[0].lower() == chosen.lower():
            print("\nMatch found:", p)
            found = True
            break

    if not found:
        print("\nSorry, that user is not in the database.")

    print("\nYour ideal date day is:", random_date_day())
    print("\nThank you for using Harry's Dating App!")

main()
