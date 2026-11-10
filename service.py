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

# GUI / layered-app helpers (same minimum data: name, weight, reference only)
def build_todays_record(user):
    """Build a plain daily record (no database details)."""
    return {
        "date": todays_date_str(),
        "weight": user["weight"],
        "cml": calc_user_cml(user["weight"], TODAYS_ACT_FACTOR),
    }

def todays_date_str():
    """Build a string representation of the current date."""
    return date.today().strftime("%d-%m-%Y")


def save_todays_user_record(user):
    """Service API: calculate today's record, then ask the repository to save it."""
    record = build_todays_record(user)
    save_daily_record(record)
    return record

def build_user_stats_message(user):
    cml = calc_user_cml(user["weight"], TODAYS_ACT_FACTOR)
    return (
        f"\nWithout any exercise at all, {user['reference']},"
        f"\nyou could consume up to {cml}kcal today"
        "\nto preserve your current weight.\n"
    )

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





# -----------------------------
# 4. MAIN PROGRAM (console version - barred for GUI app)
# -----------------------------
"""
no longer here, moved to main.py
"""
