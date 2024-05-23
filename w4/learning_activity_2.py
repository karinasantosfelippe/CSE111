"""
Author: Karina Santos Felippe
Concept: Dictionary
            - A data type that contains keys and values
            - Objects can be changed
            - They are dynamic
            - They can be nested
            - Each key must be unique within a dictionary
            - Each value does not have to be unique
"""

def microsoft_videos():
    # Dictionaries

    print("--- Dictionary's format ---")
    your_dictionary = {
        'key': 'value'
    }
    print(your_dictionary)

    print()

    # Creating
    print("--- Create a dictionary ---")
    bad_guys = {
        'daredevil': 'kingpin',
        'x-men': 'apocalypse',
        'batman': 'bane'
    }
    print(bad_guys)
    print("Index 'batman': ", bad_guys["batman"])
    print()

    print("--- Add a key value pair ---")
    bad_guys['deadpool'] = 'evil'
    print(bad_guys)

    print()

    print("--- Change an index value ---")
    bad_guys['deadpool'] = 'evil deadpool'
    print(bad_guys)

    print()

    print("--- Delete an index ---")
    del bad_guys['daredevil']
    print(bad_guys)

    print()

    # Remember to use the index name!
    # bad_guys[0] will return an Sintaxe Error
    print("--- Dictionary with decimal indexes ---")
    your_dictionary = {
        0: "plane",
        1: "train"
    }
    print("Decimal index '0': ", your_dictionary[0])

    print()    

## Lists
# Example 1
def assyngment_example_1():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

    # Add an item to the dictionary.
    students_dict["81-298-9238"] = "Sama Patel"

    # Remove an item from the dictionary.
    students_dict.pop("61-315-0160")

    # Get the number of items in the dictionary.
    length = len(students_dict)
    print(f"length: {length}")

    # Print the entire dictionary.
    print(students_dict)
    print()

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[id]

        # Print the student's name.
        print(name)

    else:
        print("No such student")
    # Create a list that contains five strings.

## Compound Values
# Example 2
def assyngment_example_2():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

## Finding One Item
# Example 3
def assyngment_example_3():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # This is a difficult and slow way to find an item in a
    # dictionary. Don't write code like this to find an item
    # in a dictionary!

    # For each item in the dictionary, check if
    # its key is the same as the variable id.
    student = None
    for key, value in students_dict.items(): # Bad example!
        if key == id:                        # Don't use a loop
            student = value                  # like this to find an
            break                            # item in a dictionary.

# Example 4
def assyngment_example_4():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]

        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[GIVEN_NAME_INDEX]
        surname = value[SURNAME_INDEX]

        # Print the student's name.
        print(f"{given_name} {surname}")

    else:
        print("No such student")

## Processing All Items
# Example 5
def assyngment_example_5():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for item in students_dict.items():
        key = item[0]
        value = item[1]

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")

# Example 6 - Improving for loop from example 5
def assyngment_example_6():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for key, value in students_dict.items():

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")

## Converting between Lists and Dictionaries
# Example 7
def assyngment_example_7():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]

    # Convert the numbers and names lists into a dictionary.
    student_dict = dict(zip(numbers_list, names_list))

    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()

    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())

    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)

def main():
    # microsoft_videos()
    # assyngment_example_1()
    # assyngment_example_2()
    # assyngment_example_3()
    # assyngment_example_4()
    # assyngment_example_5()
    # assyngment_example_6()
    assyngment_example_7()

# Call main to start this program.
if __name__ == "__main__":
    main()