"""
Author:
    Karina Santos Felippe
Problem Statement:
    A common task for many knowledge workers is to use a number, key, or ID to find information about a person. For example, a knowledge worker may use a phone number or e-mail address as a key to find (or look up) additional information about a customer. During this activity, your team will write a Python program that uses a student’s I-Number to look up the student’s name.
"""
import csv

# CONSTANTS
STUDENT_NAME_INDEX = 1
INUMBER_DIGITS = 9

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list
    # Return the dictionary.
    return dictionary

def validate_inumber(inumber):
    inumber_range = len(inumber)

    if inumber_range < INUMBER_DIGITS:
        print("Invalid I-Number: too few digits")
    elif inumber_range > INUMBER_DIGITS:
        print("Invalid I-Number: too many digits")
    elif inumber.isnumeric():
        return True
    else:
        print("Invalid I-Number")
    
    return False

def main():
    # Store the students in a compound dictionary
    dict = read_dictionary("students.csv", 0)
    print(dict)

    # Ask user to student id
    inumber_input = input("Please enter an I-Number (xxxxxxxxx): ")

    while inumber_input != "end":
        inumber = inumber_input.replace("-", "")
        if validate_inumber(inumber):
            # Print the name of the student if the id is on the list
            if inumber in dict:
                print(dict[inumber][STUDENT_NAME_INDEX])
            else:
                print("No such student")
        
        # Try again
        print("\nEnter 'end' to finish")
        inumber_input = input("Please enter an I-Number (xxxxxxxxx): ")

# Call main to start this program.
if __name__ == "__main__":
    main()