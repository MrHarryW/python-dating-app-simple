from ui import loading_screen
from validation import ageCheck, passwordCheck, get_int
from profiles import create_basic_profile, collect_list, create_interests
from database import save_user
from logic import get_partners, random_date_day

def main():
    loading_screen()

    print("Welcome to Harry's Dating App\n")

    # Age check loop
    while True:
        age = get_int("Enter your age: ")
        if ageCheck(age):
            break
        print("You must be 18 or older.")

    # Login (simple GCSE version)
    username = input("Enter username: ")
    while username != "HarryWheeler1909":
        username = input("Wrong username. Try again: ")

    password = input("Enter password (8+ chars): ")
    while not passwordCheck(password):
        password = input("Password too short. Try again: ")

    # Build profile
    profile = create_basic_profile()

    profile["holidayDestinations"] = collect_list("Enter a holiday destination: ", 3)
    profile["favouriteActivities"] = collect_list("Enter a favourite activity: ", 3)
    profile["fiveThings"] = collect_list("Enter something you can't live without: ", 5)

    profile["interests"] = create_interests()

    # Save to JSON
    save_user(profile)

    # Matching
    partners = get_partners(profile["interests"]["gender"])
    print("\nPossible matches:")
    for p in partners:
        print("-", p[0])

    chosen = input("Choose a partner: ")
    found = False
    for p in partners:
        if p[0].lower() == chosen.lower():
            print("Match found:", p)
            found = True

    if not found:
        print("Sorry, that user is not in the database.")

    print("Your ideal date day is:", random_date_day())
    print("\nThank you for using Harry's Dating App!")

main()
