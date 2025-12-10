import time

loading_steps = [
    ("Locating global servers", 3),
    ("Reading third party profile data", 3),
    ("Accessing third party login credentials", 3),
    ("Loading onboarding services", 2),
    ("Creating micro-interactions", 2),
    ("Loading profile data", 4),
    ("Loading login credentials", 3),
    ("Compiling all data", 2),
    ("Creating UI/UX", 2)
]

def loading_screen():
    print("\n////////////////////")
    print("Initiating Dating App")
    print("////////////////////\n")

    for step, seconds in loading_steps:
        for i in range(seconds * 10):
            remaining = round((seconds - i/10), 1)
            print(f"{step}... {remaining}s remaining.")
            time.sleep(0.05)

    print("\n////////////////////")
    for step, _ in loading_steps:
        print(step + ".")
    print("////////////////////\n")
