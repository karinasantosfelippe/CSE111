"""
Author: Karina Santos Felippe

Purpose: Prove that you can write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see.

Problem Statement:
    The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

    - v is the volume in liters,
    - π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
    - w is the width of the tire in millimeters,
    - a is the aspect ratio of the tire, and
    - d is the diameter of the wheel in inches.
"""

import math
from datetime import datetime

# WIDTH is the width of the tire in millimeters
width = int(input("Enter the width of the tire in mm (ex 205): "))
# ASPECT_RATIO is the aspect ratio of the tire
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
# DIAMETER is the diameter of the wheel in inches
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume using the provided formula
volume = (math.pi*(width**2)*aspect_ratio*((width*aspect_ratio)+(2540*diameter)))/10000000000

# Display the volume
print(f"\nThe approximate volume is {volume:.2f} liters.\n")

# Restrict input choices array
restrict_inputs = ["yes", "no"]

# Looping asking the options
user_input = input("Do you want to buy tires with the provided dimensions? (yes/no) ").lower()
while user_input not in restrict_inputs:
    print("Please, provide a valid answer ('yes' or 'no')\n")
    user_input = input("Do you want to buy tires with the provided dimensions? (yes/no) ").lower()

# Store the values about sale
buy_intention = user_input

# Store the phone number if the answer is positive
phone_number = 0
if user_input == "yes":
    phone_number = input("Please enter a phone number: ")
    buy_intention += f", {phone_number}"

# Store the current date and time
current_datetime = datetime.now().date()

# Open the text file in append mode
with open("volumes.txt", "at") as volumes_file:
    # Print the date, inputs, volume, intention to buy and phone number (optional) to the file
    print(current_datetime, width, aspect_ratio, diameter, f"{volume:.2f}", buy_intention, sep=", ", file=volumes_file)