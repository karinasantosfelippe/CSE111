"""
Author: Karina Felippe
Purpose: Learn and apply the new topics of the week.
"""

''' FUNCTIONS '''

# n = float(input("Please enter a number: "))
# r = round(n, 2)
# print(r)

## EXAMPLE
# FUNCTION: input(prompt) // built-in function
# ARGUMENT: "Please enter a number: "
# PARAMETER: prompt

# The code on line 1 causes the computer to call the built-in input function and then call the built-in float function.
# Line 2 causes the computer to call the built-in round function and pass two arguments. Notice that the order of the arguments matches the order of the parameters. Specifically, the number to be rounded (n) is the first argument, and the number of digits after the decimal point (2) is the second argument.
# Line 3 causes the computer to call the built-in print function to print the rounded number.

''' NAMED ARGUMENTS'''

# print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)
# Notice from the excerpt that the print function can take many objects that will be printed. Optionally, it can take parameters named sep, end, file, and flush that must be named when they are used. For example, this code calls the print function to print three words all separated by a vertical bar (|). Notice the named arguments sep and flush.

x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=True)