# -----------------------------
# 1. IMPORTS
# -----------------------------
# from random import randint, randrange
from datetime import date

from repository import save_daily_record

# -----------------------------
# 2. SETUP (CONSTANTS & LISTS & DICTIONARIES)
# -----------------------------
# always 1.2 - we are calculating CML without any daily exercise
TODAYS_ACT_FACTOR = 1.2
TITLES = {
    "Female": "dear Madam",
    "Male": "dear Sir",
}

# Using a List of Dictionaries to store user records
users = [
    {
        "name": "Anna",
        "weight": 65.0,
        "reference": "dear Madam",
    },
    {
        "name": "John",
        "weight": 82.5,
        "reference": "dear Sir",
    },
    {
        "name": "Sasha",
        "weight": 70.0,
        "reference": "dear Madam",
    },
]

# -----------------------------
# 3. FUNCTIONS
# -----------------------------
def calc_user_cml(user_weight, user_act_factor):
    bmr = user_weight * 24.2  # Basal Metabolic Rate (in kcal/day)
    return round(bmr * user_act_factor, 2)  # Calorie Maintenance Level (in kcal/day)


def input_weight_fail_proof():
    while True:
        try:
            # Check if the user input for the 'weight' variable is the correct data type
            user_weight = float(input("\nWhat is your current weight? "))
            print("\nThank you.")
            return user_weight
        except ValueError:
            # If an error occurs (like typing text instead of a float)
            print("You need to type a whole or decimal number. Try again.")


def input_sex_fail_proof():
    while True:
        # .strip() removes accidental spaces, .title() capitalizes the first letter
        sex = input("What is your sex? (Male/Female) ").strip().title()
        # Check if the user input is correct
        if sex in TITLES:
            return TITLES[sex]
        print("You need to type 'Male' or 'Female'. Try again.")


"""
def generate_a_squat_challenge():
    # Generates a random integer from 1 to 10.
    squat_number_now = randint(1, 10)
    # Generates a random integer from 20 to 100 divisible by 10.
    squat_number_today = randrange(20, 100, 10)
    print(
        "\nHow about some challenge to burn more calories? "
        f"Let's do {squat_number_now} squats right now!"
        "\n\nHow about some greater challenge to burn even more calories? "
        f"Let's do {squat_number_today} squats today!\n"
    )
"""


def print_username_letters_top_down():
    # To get your EXACT original output (letters, commas, and a trailing space),
    # we dynamically build the original string format from the new database.
    users_string = ",".join(user["name"] for user in users) + " "
    for letter in users_string:  # Does something to every letter in the variable "users"
        print(letter)  # Each letter is printed


def print_whole_usernames_top_down():  # Print existing usernames individually
    print("These are existing users: ")
    for user in users:
        print(user["name"])


def save_user_record():
    name = input("What is your name? ")
    weight = input_weight_fail_proof()
    reference = input_sex_fail_proof()
    users.append({
        "name": name,
        "weight": weight,
        "reference": reference,
    })
    print(f"User {name} has been added to the database.")


def print_my_stats():
    user_name = input("What is your username? ")
    while True:
        for user in users:
            if user["name"] == user_name:
                print(
                    f"\nWithout any exercise at all, {user['reference']},",
                    "\nyou could consume up to"
                    f" {calc_user_cml(user['weight'], TODAYS_ACT_FACTOR)}kcal today\n"
                    "to preserve your current weight.\n",
                )
                return
        print("\nUser not found. Please try again.")
        user_name = input("What is your username? ")


# GUI / layered-app helpers (same minimum data: name, weight, reference only)
def get_user_names():
    return [user["name"] for user in users]


def find_user_by_name(user_name):
    for user in users:
        if user["name"] == user_name:
            return user
    return None


def add_user(name, weight, reference):
    user = {
        "name": name,
        "weight": weight,
        "reference": reference,
    }
    users.append(user)
    return user


def build_user_stats_message(user):
    cml = calc_user_cml(user["weight"], TODAYS_ACT_FACTOR)
    return (
        f"\nWithout any exercise at all, {user['reference']},"
        f"\nyou could consume up to {cml}kcal today"
        "\nto preserve your current weight.\n"
    )


def todays_date_str():
    return date.today().strftime("%d-%m-%Y")


def build_todays_record(user):
    """Build a plain daily record (no database details)."""
    return {
        "date": todays_date_str(),
        "weight": user["weight"],
        "cml": calc_user_cml(user["weight"], TODAYS_ACT_FACTOR),
    }


def save_todays_user_record(user):
    """Service API: calculate today's record, then ask the repository to save it."""
    record = build_todays_record(user)
    save_daily_record(record)
    return record


# -----------------------------
# 4. MAIN PROGRAM (console version - barred for GUI app)
# -----------------------------
"""
def main():
    while True:
        print(
            "What do you want to do? "
            "1 Register a new user "
            "2 Print my stats "
            "3 Exit"
        )
        choice = input()
        if choice == "1":
            save_user_record()
        elif choice == "2":
            print_whole_usernames_top_down()
            print_my_stats()
        elif choice == "3":
            break
        else:
            print("Invalid choice. You must type 1-3. Please try again.")

    # generate_a_squat_challenge()
    # print_username_letters_top_down()
    # print_whole_usernames_top_down()

if __name__ == "__main__":
    main()
"""
