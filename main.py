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

print("\n\nNow on to a few more questions so that we can finish setting up your profile.\n\n")

favouriteActivities = []
for i in range(3):
  activity = input("Please enter one of your three favourite activities to partake in: ")
  favouriteActivities.append(activity)
print("\nYou have chosen:")
for x in range(len(favouriteActivities)):
  print(favouriteActivities[x])

fiveThings = []
for i in range(5):
  thing = input("Please enter one of the five things you cannot live without: ")
  fiveThings.append(thing)
print("\nYou have chosen:")
for x in range(len(fiveThings)):
  print(fiveThings[x])

print("\n\nNow that we have finished your profile, lets see what you are interested in.\n\n")

minimumAge = int(input("What is the youngest age you would be interested in? "))
if minimumAge < 18:
  print("Please note that we cannot allow people of this age on the app and therefore cannot recommend this age group.")
  minimumAge = 18
maximumAge = int(input("What is the oldest age you would be interested in? "))
if maximumAge > 25:
  print("Please note that we do not have any users above 25.")
  maximumAge = 25

print("\n\nNow that we have your age groups sorted here are a few more questions.\n\n")

preferedGender = input("Would you like to date a male or a female? ")

firsDateLocation = input("Where would you like to take someone on your first date with them? ")

print("\n\nHere is your current profile and interests:"\n\n)

print("Profile:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hair Colour:", hairColour)
print("Ethnicity:", ethnicity)
print("Occupation:", occupation)
print("Favoured Holiday Destinations:", *holidayDestinations)
print("Favoured Activities:", *favouriteActivities)
print("Five Things You Cannot Live Without:", *fiveThings)
print("Interests:")
print("Gender:", preferedGender)
print("Pefered age range for partner is:", minimumAge + "-" + maximumAge)
print("First Date Location:", firstDateLocation)

print("\n\nHere are a few funny questions to add to your profile to make people smile.\n\n")

print("We are going to create a joke, please select either a dog or cat.")
animal = input("")
if animal.lower() == "dog":
  print("What do you call a dog that is also a magician? - A labra-cadabra-dor!")
elif animal.lower() == "cat":
  print("What do you call a cat that works in business? - A purrfessional!")
else:
  print("You did nto select either of the options so you do not get a joke.")

amountOfMaltesers = int(input("\nHow many maltesers can you fit in your mouth? "))
if amountOfMaltesers <= 10:
  print("Good Job!")
elif amountOfMaltesers > 10:
  print("You Need Help.")

seeProfile = input("Would you like to see your final profile?")
if seeProfile.lower() == 'yes':
  print("Profile:")
  print("Name:", name)
  print("Age:", age)
  print("Height:", height)
  print("Hair Colour:", hairColour)
  print("Ethnicity:", ethnicity)
  print("Occupation:", occupation)
  print("Favoured Holiday Destinations:", *holidayDestinations)
  print("Favoured Activities:", *favouriteActivities)
  print("Five Things You Cannot Live Without:", *fiveThings)
  print("Interests:")
  print("Gender:", preferedGender)
  print("Pefered age range for partner is:", minimumAge + "-" + maximumAge)
  print("First Date Location:", firstDateLocation)
  print("Jokes/Amusing Section:")
  print(name, "selected", animal.lower())
  print(name, "can fit", amountOfMaltesers, "in there mouth.")

potentialFemalePartners = [
  ["Alice", 25, "London"],
  ["Janet", 21, "Dartford"],
  ["Rosie", 19, "Cambridge"]
]

potentialMalePartners = [
  ["James", 25, "Oxford"],
  ["John", 22, "London"],
  ["Arham", 19, "Dartford"]
]

if preferedGender.lower() == 'male':
  print("\n\nSince you chose male as your prefered gender here are our available candidates:")
  for i in potentialMalePartners:
    print(i[0])
  print("Please note some of these may be out of your age range, but out algorithm has selected them as a good match for you.")
  chosenPartner = input("Please name your chosen candidate: ")
  for option in potentialMalePartners:
    if option[0] == chosenPartner:
      print(*option)
    else:
      print("Sorry this user is not in our database.")
elif preferedGender.lower() == 'female':
  print("\n\nSince you chose female as your prefered gender here are our available candidates:")
  for i in potentialFemalePartners:
    print(i[0])
  print("Please note some of these may be out of your age range, but out algorithm has selected them as a good match for you.")
  chosenPartner = input("Please name your chosen candidate: ")
  for option in potentialFemalePartners:
    if option[0] == chosenPartner:
      print(*option)
    else:
      print("Sorry this user is not in our database.")  

  daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
  randomDay = random.choice(daysOfTheWeek)
  print("\nIf you found a user the best day for the date is", randomDay)

  print("\n\nThank you for using Harry's Dating App!")

  break
