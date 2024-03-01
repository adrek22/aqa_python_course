# Multiline comments using double quotes
"""
My Homework
Variables
"""

# Variables
dob_day = 15
dob_month = 'May'
dob_year = 1984

# Multiline comments using single quote
'''
Constants
'''

DAYS_IN_COMMON_YEAR = 365
MY_NAME = 'Mykhailo'


# Function to display a message
def show_message():
    # Using variables inside function
    print("Hello, my name is " + MY_NAME + ".")
    print(f"My Date of Birth is {dob_day} {dob_month} {dob_year}")


# Simple class with Pascal Case or Upper Camel Case name
class SimpleClass:
    # Simple method
    def simple_method(self):
        print("This is a simple method.", 'str\ning2', sep='***', end='123')


# Function call
show_message()

my_simple_object = SimpleClass()
my_simple_object.simple_method()  # This will print a text
