from validation import get_int

def create_basic_profile():
    name = input("Please enter your name: ")
    age = get_int("Enter your age: ")
    height = get_int("Enter your height in cm: ")
    hair = input("Enter your hair colour: ")
    ethnicity = input("Enter your ethnicity: ")
    occupation = input("Enter your current occupation: ")

    return {
        "name": name,
        "age": age,
        "height": height,
        "hairColour": hair,
        "ethnicity": ethnicity,
        "occupation": occupation
    }


def collect_list(prompt, count):
    items = []
    for _ in range(count):
        items.append(input(prompt))
    return items


def create_interests():
    min_age = get_int("Minimum age you're interested in: ")
    if min_age < 18:
        print("We cannot allow profiles younger than 18. Setting to 18.")
        min_age = 18

    max_age = get_int("Maximum age you're interested in: ")
    if max_age > 25:
        print("We don't have users older than 25. Setting to 25.")
        max_age = 25

    gender = input("Preferred gender (male/female): ")
    date_location = input("Where would you go for a first date? ")

    return {
        "ageRange": [min_age, max_age],
        "gender": gender,
        "firstDateLocation": date_location
    }
