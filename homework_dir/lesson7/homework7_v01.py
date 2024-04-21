""" Homework 7 """


def my_map(func, *iterables) -> list:
    """ Custom implementation of the map function """
    return [func(*items) for items in zip(*iterables)]


def my_filter(func, iterable) -> list:
    """ Custom implementation of the filter function """
    return [item for item in iterable if func(item)]


def task1():
    """Demonstrate custom and built-in map and filter functions side by side."""
    # Function for map
    merge_or_add = lambda x, y: x + y
    prefixes = ['py', 'program', 'lang', 1, -2.2, True]
    suffixes = ['thon', 'ming', 'uage', -1, -7.8, False]

    custom_map_results = my_map(merge_or_add, prefixes, suffixes)
    built_in_map_results = map(merge_or_add, prefixes, suffixes)

    print("Results of custom vs. built-in map function:")
    for index, (custom_item, built_in_item) in enumerate(zip(custom_map_results, built_in_map_results)):
        print(f"{index}: {custom_item} || {built_in_item}")

    print("-" * 80)  # Separator for readability

    # Function for filter
    is_str_or_int = lambda x: isinstance(x, str) or isinstance(x, int)
    mixed_list = ['python', 3.14, -2, 'hello', 42, False, 'world', 3.5]

    custom_filter_results = my_filter(is_str_or_int, mixed_list)
    built_in_filter_results = filter(is_str_or_int, mixed_list)

    print("Results of custom vs. built-in filter function:")
    for index, (custom_item, built_in_item) in enumerate(zip(custom_filter_results, built_in_filter_results)):
        print(f"{index}: {custom_item} || {built_in_item}")


def power_of_x(x: int):
    """Returns a lambda function that raises its argument y to the power of x."""
    return lambda y: y ** x


def task2():
    """Demonstrate a function with lambda function."""
    # User to enter the value for y and x
    y = int(input("Enter the value of y (the base): "))
    x = int(input("Enter the value of x (the exponent): "))

    power_of_x_func = power_of_x(x)
    print(f"{y} raised to the power of {x} is: {power_of_x_func(y)}")


def greet():
    print("Hello, there!")


def square(num=2):
    return f"Square of {num} is: {num ** 2}"


def length(string='string'):
    return f"Length of \'{string}\' is: {len(string)}"


def is_even(num=2):
    var = f"{num} is even" if num % 2 == 0 else f"{num} is odd"
    return var


def reverse_string(string='gnirts'):
    return f"Reverse of \'{string}\' is: {string[::-1]}"


def task3():
    """Demonstrate the execution of a defined function entered by user."""
    result = eval(input("Enter a function name: "))
    if result is not None:
        print(result)


# Main Flow. User to enter the task number
task_number = input("Please select a task from 1 to 3: ")

# Execute the corresponding task or notify the user of invalid input
match task_number:
    case '1':
        task1()
    case '2':
        task2()
    case '3':
        task3()
    case _:
        print("Invalid input. Please enter 1, 2, or 3.")
