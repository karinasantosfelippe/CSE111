"""
Author: Karina Santos Felippe
Concept: Handling Exceptions
    Errors and exceptional situations sometimes occur while a program is running. Such errors include a program attempting to read from a file that doesn’t exist, a connection error when connecting to a server on a network, data that cannot be found on a server, and calculations that produce undefined results. A well written program doesn’t crash when an error occurs but instead handles errors in a graceful manner that may include adjusting to an error, printing an error message for the user to see, and saving an error message to a log file. During this lesson, you will learn to write code that handles errors that may occur while your Python program is running.
"""

def microsoft_videos():
    # Catching runtime errors
    try:
        print(x/y)
    except ZeroDivisionError as e:
        print("Zero Division Error, e: ", e)
    except:
        print("Sorry, something went wrong")
    finally:
        print("This always runs on success or failure")
        
    print()
    # Catching runtime errors
    try:
        x = 42
        y = 0
        print(x/y)
    except ZeroDivisionError as e:
        print("Not allowed to divide by zero. Exception: ", e)
    except:
        print("Sorry, something went wrong")
    finally:
        print("This always runs on success or failure")

## Errors
# Example 1
def assyngment_example_1():
    # Example 1
    try:
        # Write normal code here. This block must include
        # code that falls into two groups:
        # 1. Code that may cause an exception to be raised
        # 2. Code that depends on the results of the code
        #    in the first group
        print()
    except ZeroDivisionError as zero_div_err:
        # Code that the computer executes if the code in the try
        # block caused a function to raise a ZeroDivisionError.
        print()
    except ValueError as val_err:
        # Code that the computer executes if the code in the
        # try block caused a function to raise a ValueError.
        print()
    except (TypeError, KeyError, IndexError) as error:
        # Code that the computer executes if the code in the
        # try block caused a function to raise a TypeError,
        # KeyError, or IndexError.
        print()
    except Exception as excep:
        # Code that the computer executes if the code in the try
        # block caused a function to raise any exception that
        # was not handled by one of the previous except blocks.
        print()
    except:
        # Code that the computer executes if the code in the
        # try block caused a function to raise anything that
        # was not handled by one of the previous except blocks.
        print()
    else:
        # Code that the computer executes after the code
        # in the try block if the code in the try block
        # did not cause any function to raise an exception.
        print()
    finally:
        # Code that the computer executes after all the other
        # code in try, except, and else blocks regardless of
        # whether an exception was raised or not.
        print()

# Example 2 - Type Error
def assyngment_example_2():
    try:
        text = input("Please enter a number: ")
        integer = round(text)
        print(integer)
    except TypeError as type_err:
        print(type_err)

# Example 3 - Value Error
def assyngment_example_3():
    try:
        number = float(input("Please enter a number: "))
        print(number)
    except ValueError as val_err:
        print(val_err)

# Example 4 - Zero Division Error
def assyngment_example_4():
    try:
        players = int(input("Enter the number of players: "))
        teams = int(input("Enter the number of teams: "))
        players_per_team = players / teams
        print(f"Each team should have {players_per_team} players")
    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)

# Example 5 - Index Error
def assyngment_example_5():
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]
        # Attempt to change the surname at index 3. Because
        # there are only three names in the surnames list and
        # therefore the last index is 2, this statement will
        # fail and cause the computer to raise an IndexError.
        surnames[3] = "Olsen"
        # Attempt to print the surname at index 3. Because
        # there are only three names in the surnames list and
        # therefore the last index is 2, this statement will
        # fail and cause the computer to raise an IndexError.
        print(surnames[3])
    except IndexError as index_err:
        print(index_err)

# Example 7 - Key Error
def assyngment_example_7():
    try:
        # Create a dictionary with student IDs as
        # the keys and student names as the values.
        students = {
            "42-039-4736": "Clint Huish",
            "61-315-0160": "Amelia Davis",
            "10-450-1203": "Ana Soares",
            "75-421-2310": "Abdul Ali",
            "07-103-5621": "Amelia Davis"
        }
        # Attempt to find the key "50-420-1021",
        # which is not in the dictionary. This will
        # cause the computer to raise a KeyError.
        name = students["50-420-1021"]
        print(name)
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

# Example 8 - File Not Found Error
def assyngment_example_8():
    try:
        with open("products.vcs", "rt") as products_file:
            for row in products_file:
                print(row)
    except FileNotFoundError as not_found_err:
        print(not_found_err)

# Example 9 - Permission Error
def assyngment_example_9():
    try:
        with open("contacts.csv", "rt") as contacts_file:
            for row in contacts_file:
                print(row)
    except PermissionError as perm_err:
        print(perm_err)

# Example 12 - Validating User Input
def assyngment_example_12():
    gender = input("Enter your gender (M or F): ")
    weight = get_float("Enter your weight in kg: ", 20, 500)
    height = get_float("Enter your height in cm: ", 60, 250)
    age = get_float("Enter your age in years: ", 10, 120)
    bmr = basal_metabolic_rate(gender, weight, height, age)
    print(f"Your basal metabolic rate is {bmr} calories per day.")
def get_float(prompt, lower_bound, upper_bound):
    """Get a number from the user, validate that the user
    entered a number and not some other text, validate that
    the number is between a lower and upper bound, and then
    return the number. If the user enters an invalid number,
    this function will prompt the user repeatedly until the
    user enters a valid number.
    Parameters
        prompt: A string to display to the user.
        lower_bound: The smallest number that the user may enter.
        upper_bound: The largest number that the user may enter.
    Return: The number entered by the user.
    """
    while True:
        try:
            text = input(prompt)
            number = float(text)
            if number < lower_bound:
                print(f"{number} is too small.")
                print("Please enter another number.")
            elif number > upper_bound:
                print(f"{number} is too large.")
                print("Please enter another number.")
            else:
                # If the computer gets to this line of code,
                # the user entered a valid number between
                # lower_bound and upper_bound, so exit the loop.
                break
        except ValueError as val_err:
            # The user entered at least one character that is
            # not part of a floating point number, so print a
            # message asking the user to enter a number.
            print(f"{text} is not a number.")
            print("Please enter a number.")
    return number
def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate
    in calories per day. weight must be in kilograms, height
    must be in centimeters, and age must be in years.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight \
                + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight \
                + 4.799 * height - 5.677 * age
    return bmr

def main():
    # microsoft_videos()
    # assyngment_example_1()
    # assyngment_example_2()
    # assyngment_example_3()
    # assyngment_example_4()
    # assyngment_example_5()
    # assyngment_example_7()
    # assyngment_example_8()
    # assyngment_example_9()
    assyngment_example_12()

# Call main to start this program.
if __name__ == "__main__":
    main()