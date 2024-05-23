"""
Author:
    Karina Santos Felippe
Purpose:
    There are a few details about writing and calling functions in Python that, if you understand, will help you be a more effective programmer. These details include default parameter values and pass by reference. As a team during this activity, you will write and call a function that demonstrates both default parameter values and pass by reference.
"""
import random

def main():
    # Creates a list named numbers and print it
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    # Calls the append_random_numbers function with
    # only one argument to add one number to numbers
    append_random_numbers(numbers)
    print(numbers)

    # Calls the append_random_numbers function again
    # with two arguments to add three numbers to numbers
    append_random_numbers(numbers, 3)
    print(numbers)

    # Create a list of words
    words_list = []
    
    # Call the append_random_words function and
    # print the list of words
    append_random_words(words_list)
    print(words_list)
    append_random_words(words_list, 3)
    print(words_list)

# Has two parameters: a list named numbers_list and
# an integer named quantity. The parameter quantity
# has a default value of 1
def append_random_numbers(numbers_list, quantity = 1):
    # Create a loop that appends quantity random numbers at the end of numbers_list
    for _ in range(quantity):
        # Computes quantity pseudo random numbers
        # by calling the random.uniform function
        random_number = random.uniform(0, 100)

        # Rounds the quantity pseudo random numbers
        # to one digit after the decimal.
        rounded = round(random_number, 1)

        # Appends the quantity pseudo random numbers
        # onto the end of the numbers_list.
        numbers_list.append(rounded)

def append_random_words(words_list, quantity = 1):
    words_options = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

    for _ in range(quantity):
        # Randomly selects quantity words from a list
        # of words and appends the selected words at
        # the end of words_list
        word = random.choice(words_options)
        words_list.append(word)

# If this file was executed like this:
# > python file_name.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
