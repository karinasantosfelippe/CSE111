"""
Author:
    Karina Santos Felippe
Problem Statement:
    A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.
"""
import csv

# CONSTANTS
PRODUCT_FILE_NAME = "products.csv"
REQUEST_FILE_NAME = "request.csv"
PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
REQUEST_PRODUCT_ID_INDEX = 0
REQUEST_QUANTITY_INDEX = 1

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
    print("All Products")
    products_dict = read_dictionary(PRODUCT_FILE_NAME, PRODUCT_ID_INDEX)
    print(products_dict)

    print("Requested Items")
    with open(REQUEST_FILE_NAME, "rt") as request_file:
        rows_list = csv.reader(request_file)
        next(rows_list)
        for item in rows_list:
            if len(item) != 0:
                corresponding_index = item[REQUEST_PRODUCT_ID_INDEX]
                product = products_dict[corresponding_index]
                print(f"{product[PRODUCT_NAME_INDEX]}: {item[REQUEST_QUANTITY_INDEX]} @ {product[PRODUCT_PRICE_INDEX]}")

# Call main to start this program.
if __name__ == "__main__":
    main()