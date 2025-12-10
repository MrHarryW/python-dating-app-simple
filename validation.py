def ageCheck(age):
    return age >= 18

def passwordCheck(password):
    return len(password) >= 8

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")
