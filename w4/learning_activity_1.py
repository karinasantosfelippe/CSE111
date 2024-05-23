"""
Author: Karina Santos Felippe
Concept: List
    
"""

def microsoft_videos():
    ''' Lists and Arrays '''
    # Lists:
    #   store anything
    #   store any type
    print("--- Lists are collections of items ---")

    names = ['Christopher', 'Susan']
    scores = []
    scores.append(98) # Add new item to the end
    scores.append(99)
    print(names)
    print(scores)
    print(scores[1]) # Collections are zero-indexed

    print()

    # Arrays:
    #   numerical data types
    #   must all be the same type
    print("--- Arrays are also collections of tiems ---")

    from array import array
    scores = array('d')
    scores.append(97)
    scores.append(98)
    print(scores)
    print(scores[1])

    print()

    # Common operations
    print("-- Common operations ---")

    names = ['Susan', 'Çhristopher']
    print(len(names)) # Get the number of items
    names.insert(0, 'Bill') # Insert before index
    print(names)
    names.sort()
    print(names)

    print()

    # Retrieving ranges
    print("--- Retrieving ranges ---")

    names = ['Susan', 'Christopher', 'Bill', 'Justin']
    presenters = names[1:3] # Start and end index
    print(names)
    print(presenters)

    print()

    # Dictionaries:
    #   Key/Value pairs
    #   Storage order not guaranteed
    # What's the difference?
    # Lists:
    #   Zero-based index
    #   Storage order guaranteed
    print("--- Dictionaries ---")

    person = {'first': 'Christopher'}
    person['last'] = 'Harrison'
    print(person)
    print(person['first'])

    print()

    # Loop through a collection
    for name in ['Christopher', 'Susan']:
        print(name)
    
    print()

## Lists
# Example 1
def assyngment_example_1():
    # Create a list that contains five strings.
    colors = ["yellow", "red", "green", "yellow", "blue"]
    print(colors)

    # Call the built-in len function
    # and print the length of the list.
    length = len(colors)
    print(f"Number of elements: {length}")

    # Print the element that is stored
    # at index 2 in the colors list.
    print("Index 2: ", colors[2])

    # Change the element that is stored at
    # index 3 from "yellow" to "purple".
    colors[3] = "purple"
    print("Change index 3 to 'purple'")

    # Print the entire colors list.
    print(colors)

# Example 2
def assyngment_example_2():
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    print(fabrics)

    print("\n---> Insert an element at the beginning of the fabrics list.")
    fabrics.insert(0, "chiffon")
    print(fabrics)

    print("\n---> Determine if gingham is in the fabrics list.")
    if "gingham" in fabrics:
        print("gingham is in the list.")
    else:
        print("gingham is NOT in the list.")

    print("\n---> Get the index where velvet is stored in the fabrics list.")
    i = fabrics.index("velvet")
    print(i)

    print("\n---> Replace velvet with taffeta.")
    fabrics[i] = "taffeta"
    print(fabrics)

    print("\n---> Remove denim from the fabrics list.")
    fabrics.remove("denim")
    print(fabrics)

    print("\n---> Remove the last element from the fabrics list.")
    fabrics.pop()
    print(fabrics)

    print("\n---> Get the length of the fabrics list and print it.")
    n = len(fabrics)
    print(f"The fabrics list contains {n} elements.")
    print(fabrics)

## Repetion
# Example 3 - for loop
def assyngment_example_3():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)

# Example 4 - range function
def assyngment_example_4():
    print("---> Count from zero to nine by one.")
    for i in range(10):
        print(i)
    print()

    print("---> Count from five to nine by one.")
    for i in range(5, 10):
        print(i)
    print()

    print("---> Count from zero to eight by two.")
    for i in range(0, 10, 2):
        print(i)
    print()

    print("---> Count from 100 down to 70 by three.")
    for i in range(100, 69, -3):
        print(i)

# Example 5
def assyngment_example_5():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)

    print()

    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]

        print(color)

# Example 6 - break statement
def assyngment_example_6():
    sum = 0

    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number

    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")

# Example 7 - while loop
def assyngment_example_7():
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]

    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index}")

def compare_lists(list1, list2):
    """Compare the contents of two lists. If the contents
    of the two lists are not equal, return the index of
    the first difference. If the contents of the two lists
    are equal, return -1.

    Parameters
        list1: a list
        list2: another list
    Return: an index or -1
    """
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)

    # Begin at the first index (0) and repeat until the
    # computer finds two elements that are not equal or
    # until the computer reaches the end of the shortest
    # list, whichever comes first.
    i = 0
    while i < limit:
        # Retrieve one element from each list.
        element1 = list1[i]
        element2 = list2[i]

        # If the two elements are not
        # equal, quit the while loop.
        if element1 != element2:
            break

        # Add one to the index variable.
        i += 1

    # If the length of both lists are equal and the
    # computer verified that all elements are equal,
    # set i to -1 to indicate that the contents of
    # the two lists are equal.
    if length1 == length2 == i:
        i = -1

    return i

## Compound Lists
# Example 8
def assyngment_example_8():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]

    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]

    # Print the tree's height.
    print(f"height: {height}")

# Example 9
def assyngment_example_9():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    total_fruit_amount = 0

    # This loop will repeat once for each inner list
    # in the apple_tree_data compound list.
    for inner_list in apple_tree_data:

        # Retrieve the fruit amount from
        # the current inner list.
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]

        # Print the fruit amount for the current tree.
        print(fruit_amount)

        # Add the current fruit amount to the total.
        total_fruit_amount += fruit_amount

    # Print the total fruit amount.
    print(f"Total fruit amount: {total_fruit_amount:.1f}")

## Values and References
# Example 10
def assyngment_example_10():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")

# Example 11
def assyngment_example_11():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")

## Pass by Value and Pass by Reference
# Example 12
def assyngment_example_12():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"After calling modify_args():  x {x}  lx {lx}")

def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"   After changing n and alist:  n {n}  alist {alist}")

def main():
    # microsoft_videos()
    # assyngment_example_1()
    # assyngment_example_2()
    # assyngment_example_3()
    # assyngment_example_4()
    # assyngment_example_5()
    # assyngment_example_6()
    # assyngment_example_7()
    # assyngment_example_8()
    # assyngment_example_9()
    # assyngment_example_10()
    # assyngment_example_11()
    assyngment_example_12()

# Call main to start this program.
if __name__ == "__main__":
    main()