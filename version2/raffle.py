"""Randomly pick customer and print customer info"""

from random import choice
import customers

def print_random_customer(customers_file_path):
    """Take txtfile of customers and print random customer's info"""

    # Generate list of all customer objects from file
    customers_list = customers.get_customers_from_file(customers_file_path)

    # Choose random customer object from list
    rand_customer = choice(customers_list)
    
    # Print all of random customer's attributes
    print(rand_customer.__dict__)