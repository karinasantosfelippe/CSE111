"""
Author: Karina Santos Felippe
Problem Statement: 
    You work for a retail store that wants to increase sales on Tuesday and Wednesday,
    which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s
    subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
"""

''' CORE REQUIREMENTS '''
# Import the datetime class from the datetime module so that we can use just the now() and weekday() functions
from datetime import datetime

sales_days = [1,2]
discount = 0.10
tax_rate = 0.06

subtotal_input = float(input("Please enter the subtotal: "))

# Store the current date and time
current_datetime = datetime.now()
# Store the current day of week as an integer (Monday will start in 0)
current_day = current_datetime.weekday()

# Apply discount according to the rules
subtotal = subtotal_input
if subtotal_input>=50 and current_day in sales_days:
    discount_amount = subtotal*discount
    print(f"Discount amount: {discount_amount:.2f}")
    subtotal -= discount_amount

# Calculate and display sales tax amount
sales_tax = subtotal * tax_rate
print(f"Sales tax amount: {sales_tax:.2f}")

# Calculate and display the total
total = subtotal + sales_tax
print(f"Total: {total:.2f}")


''' STRETCH CHALLENGES '''

'''
    2. Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.
'''
subtotal_input = 0
print("\nEnter the price and quantity for each item.")
price = float(input("\nPlease enter the price: "))
while price != 0:
    # Get the quantity from the user.
    quantity = int(input("Please enter the quantity: "))

    subtotal_input += price * quantity

    # Print a blank line.
    print()
    
    # Get the price from the user.
    price = float(input("Please enter the price: "))

# Round the subtotal to two digits after
# the decimal and print the subtotal.
subtotal_input = round(subtotal_input, 2)
print(f"\nSubtotal: {subtotal_input:.2f}")

# Apply discount according to the rules
subtotal = subtotal_input
if subtotal_input>=50 and current_day in sales_days:
    discount_amount = subtotal*discount
    print(f"Discount amount: {discount_amount:.2f}")
    subtotal -= discount_amount

# Calculate and display sales tax amount
sales_tax = subtotal * tax_rate
print(f"Sales tax amount: {sales_tax:.2f}")

# Calculate and display the total
total = subtotal + sales_tax
print(f"Total: {total:.2f}")


'''
    1. Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing enough to receive the discount. This added code should compute and print the difference between $50 and the subtotal which is the additional amount the customer would need to purchase in order to receive the discount.
'''

if subtotal_input<50 and current_day in sales_days:
    total = 50-subtotal_input
    print(f"To receive the discount, add ${(total):.2f} to your order.")