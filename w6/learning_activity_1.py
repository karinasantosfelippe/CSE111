

### Procedural Progamming
# Example 1
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")
    declarative_function()
# Call main to start this program.
if __name__ == "__main__":
    main()

### Declarative Programming
# -- Example 2
# SELECT AVG(numbers) FROM table;

### Functional Programming
# Example 3
from functools import reduce
def declarative_function():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")

### Object-Oriented Programming
# Example 4
def object_oriented_function():
    '''Python lists and dictionaries 
    are objects and have attributes 
    and methods. Readers and Writers 
    from the csv module are also objects.
    This code uses the dot operator (.) 
    to call the append method.
    '''
    numbers = [87, 95, 72, 92, 95, 88, 84]
    numbers.append(78)
    numbers.append(72)
    print(numbers)