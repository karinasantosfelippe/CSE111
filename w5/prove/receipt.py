"""
Author:
    Karina Santos Felippe
Problem Statement:
    A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.
Assingment:
    During the prove milestone for the previous lesson, you wrote the part of this program that reads and processes two CSV files, one named products.csv that contains a catalog of products and one named request.csv that contains a customer’s order. During this prove assignment, you will add code to finish printing a receipt and to handle any exceptions that might occur while your program is running. Specifically, your program must do the following:
        - Print the store name at the top of the receipt.
        - Print the list of ordered items.
        - Sum and print the number of ordered items.
        - Sum and print the subtotal due.
        - Compute and print the sales tax amount. Use 6% as the sales tax rate.
        - Compute and print the total amount due.
        - Print a thank you message.
        - Get the current date and time from your computer’s operating system and print the current date and time.
        - Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""
import csv
from datetime import datetime

# CONSTANTS
PRODUCT_FILE_NAME = "products.csv"
REQUEST_FILE_NAME = "request.csv"
PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
REQUEST_PRODUCT_ID_INDEX = 0
REQUEST_QUANTITY_INDEX = 1
STORE_NAME = "Inkom Emporium"
SALES_TAX_RATE = 0.06

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
    response_dictionary = {}

    with open(filename, "rt") as csv_file:
        rows_list = csv.reader(csv_file)

        # Skip the header
        next(rows_list)

        for item in rows_list:
            if len(item) != 0:
                key = item[key_column_index]
                response_dictionary[key] = item
    
    return response_dictionary

def main():
    try:
        products_dict = read_dictionary(PRODUCT_FILE_NAME, PRODUCT_ID_INDEX)

        print(STORE_NAME)
        current_date_and_time = datetime.now()
        current_weekday = current_date_and_time.weekday()
        discount_amount = 1
        if current_weekday == 1 or current_weekday == 2:
            print("Today you will receive a discount in the product prices!")
            discount_amount = 0.9
        items_count = 0
        subtotal = 0
        with open(REQUEST_FILE_NAME, "rt") as request_file:
            rows_list = csv.reader(request_file)
            next(rows_list)
            for item in rows_list:
                if len(item) != 0:
                    corresponding_index = item[REQUEST_PRODUCT_ID_INDEX]
                    product = products_dict[corresponding_index]
                    quantity = int(item[REQUEST_QUANTITY_INDEX])
                    items_count += quantity
                    price = float(product[PRODUCT_PRICE_INDEX])
                    price = round((price*discount_amount), 2)
                    subtotal += (quantity * price)
                    print(f"{product[PRODUCT_NAME_INDEX]}: {quantity} @ {price}")
        
        print(f"Number of Items: {items_count}")
        print(f"Subtotal: {subtotal:.2f}")

        sales_tax_amount = subtotal * SALES_TAX_RATE
        print(f"Sales tax: {sales_tax_amount:.2f}")

        total_amount = subtotal + sales_tax_amount
        print(f"Total: {total_amount:.2f}")

        print(f"Thank you for shopping at the {STORE_NAME}.")

        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
    except FileNotFoundError as not_found_err:
        print("Error: missing file", not_found_err, sep="\n")
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file", key_err, sep="\n")
    except PermissionError as perm_err:
        print(perm_err)
    except TypeError as type_err:
        print(type_err)

# Call main to start this program.
if __name__ == "__main__":
    main()