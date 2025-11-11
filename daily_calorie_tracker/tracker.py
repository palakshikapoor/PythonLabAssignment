# ----------------------------------------------------------
# Project: Daily Calorie Tracker
# Author: Palakshi Kapoor

# Description: A simple CLI tool to log meals, track calories,
#              compare against a daily limit, and save session logs.
# ----------------------------------------------------------

import datetime

print("\n======================================")
print("      Welcome to Daily Calorie Tracker")
print("======================================")
print("This tool helps you log your meals, calculate your total calorie intake,")
print("compare it with your daily limit, and optionally save your session log.\n")

# -------------------------------
# Task 2: Input & Data Collection
# -------------------------------

# Lists to store meal names and calorie values
meals = []
calories = []

# Ask user how many meals they want to log
num_meals = int(input("How many meals would you like to log today? "))

for i in range(num_meals):
    print(f"\nMeal #{i+1}")
    meal_name = input("Enter meal name (e.g., Breakfast, Lunch): ")
    calorie_value = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_value)

# -------------------------------
# Task 3: Calorie Calculations
# -------------------------------

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# -------------------------------
# Task 4: Exceed Limit Warning System
# -------------------------------

if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit!"
else:
    status_message = "✅ Great job! You are within your daily calorie limit."

# -------------------------------
# Task 5: Neatly Formatted Output
# -------------------------------

print("\n======================================")
print("        Daily Calorie Summary")
print("======================================")
print(f"{'Meal Name':<15}\t{'Calories'}")
print("--------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:<15}\t{calories[i]:.2f}")

print("--------------------------------------")
print(f"{'Total:':<15}\t{total_calories:.2f}")
print(f"{'Average:':<15}\t{average_calories:.2f}")
print("--------------------------------------")
print(status_message)
print("======================================\n")

# -------------------------------
# Task 6 (Bonus): Save Session Log
# -------------------------------

save_option = input("Would you like to save this session to a log file? (yes/no): ").strip().lower()

if save_option == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log.txt"

    with open(filename, "w") as file:
        file.write("======================================\n")
        file.write("        Daily Calorie Summary\n")
        file.write("======================================\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        file.write(f"{'Meal Name':<15}\t{'Calories'}\n")
        file.write("--------------------------------------\n")

        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}\t{calories[i]:.2f}\n")

        file.write("--------------------------------------\n")
        file.write(f"{'Total:':<15}\t{total_calories:.2f}\n")
        file.write(f"{'Average:':<15}\t{average_calories:.2f}\n")
        file.write("--------------------------------------\n")
        file.write("======================================\n")

    print(f"\n💾 Session successfully saved to {filename}\n")
else:
    print("\nSession not saved. Goodbye!\n")
