import random

female_partners = [
    ["Alice", 25, "London"],
    ["Janet", 21, "Dartford"],
    ["Rosie", 19, "Cambridge"]
]

male_partners = [
    ["James", 25, "Oxford"],
    ["John", 22, "London"],
    ["Arham", 19, "Dartford"]
]

def get_partners(gender):
    if gender.lower() == "male":
        return male_partners
    else:
        return female_partners

def random_date_day():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return random.choice(days)
