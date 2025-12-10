import time 

print("\n////////////////////\nInitiating Dating App\n////////////////////\n") 
time.sleep(3)

for x in range(120,0,-1):
  if x <= 120 and x > 96:
    print("Locating global servers.", (x-96)/20, "seconds remaining.")
  elif x <= 96 and x > 75:
    print("Reading third party profile data.", (x-75)/20, "seconds remaining.")
  elif x <= 75 and x > 68:
    print("Accessing third party login credentials.", (x-68)/20, "seconds remaining.")
  elif x <= 68 and x > 54:
    print("Loading onboarding services.", (x-54)/20, "seconds remaining.")
  elif x <= 54 and x > 48:
    print("Creating Micro-interactions.", (x-48)/20, "seconds remaining.")
  elif x <= 48 and x > 30:
    print("Loading profile data.", (x-30)/20, "seconds remaining.")
  elif x <= 30 and x > 21:
    print("Loading login credentials.", (x-21)/20, "seconds remaining.")
  elif x <= 21 and x > 10:
    print("Compiling all data.", (x-10)/20, "seconds remaining.")
  else:
    print("Creating UI/UX.", x/20, "seconds remaining.")
  time.sleep(0.05)

time.sleep(1)
print("\n////////////////////\nLocated global servers.\nRead third party profile data.\nAccessed third party login credentials.\nLoaded onboarding services.\nCreated micro-interactions\nLoaded profile data.\nLoaded login crednetials.\nCreated UI/UX.\n////////////////////\n") 
  
def ageCheck(age):
  if age <= 18:
    print("You must be 18 years old to use this app.")
    return False
  else:
    return True

def passwordCheck(password):
  if len(password) < 8:
    print("Password length is too short")
    return False
  else:
    return True

time.sleep(1)

print("\n////////////////////")
print("Welcome to Harry's Dating App")
print("////////////////////\n")


while True:
  print("\nBefore continuing please enter an age for us to validate you access.")
  age = int(input("\nEnter your age: "))
  if ageCheck(age):
    years = age
    months = years * 12
    weeks = years * 52
    days = weeks * 7
    hours = days * 24
    print("\nWow! You have experienced:\n", years, "years.\n", months, "months.\n", weeks, "weeks.\n", days, "days.\n", hours, "hours.\n\nAnyway...")
    break
  else:
    print("Enter a valid age.")

username = ""
while username != "HarryWheeler1909":
  username = input("\nEnter username: ")
  if username != "HarryWheeler1909":
    print("\nWrong username please try again.")

password = ""
while True:
  password = input("Please enter your password. (Minimum of 8 characters): ")
  if passwordCheck(password):
    break
  else:
    print("Password too short, please try again.")

name = input("Please enter your name: ")
age = age
height = int(input("\nPlease enter your height in cm: "))
hairColour = input("\nPlease enter your hair colour: ")
ethnicity = input("\nPlease enter your ethnicity: ")
occupation = input("\nWhat is your current occupation: ")
print("\n")

holidayDestinations = []
for i in range(3):
  holidayLocation = input("Please enter a holiday destination you would like to go: ")
  holidayDestinations.append(holidayLocation)
print("\nYou have chosen:")
for x in range(len(holidayDestinations)):
  print(holidayDestinations[x])

print("Here is your current profile:\n\n")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hair Colour:", hairColour)
print("Ethnicity:", ethnicity)
print("Occupation:", occupation)
print("Favoured Holiday Destinations:", *holidayDestinations)



