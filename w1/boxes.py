"""
Author: Karina Santos Felippe
Problem:
    In our modern world economy, many items are manufactured in large factories, then packed in boxes and shipped to distribution centers and retail stores. A common question for employees who pack items is “How many boxes do we need?”
"""

# Import the math module so that we can call the math.ceil function
import math

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
boxes = items/items_per_box

print(f"\nFor { items } items, packing { items_per_box } items in each box, you will need { math.ceil(boxes) } boxes.")