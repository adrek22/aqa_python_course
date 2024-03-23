""" Homework 9. Iterator, generator """


def my_range(start: int, stop: int, step=1):
    """ Custom implementation of the range function """
    # Handle 0 for step
    if step == 0:
        raise ValueError("Step must not be zero")
    value = start
    if step > 0:
        while value < stop:
            yield value
            value += step
    else:  # Handle negative step values
        while value > stop:
            yield value
            value += step


def task1():
    """Demonstrate custom and built-in range functions side by side."""
    # Enter here data you want to demonstration
    examples = [
        (-1, 10, 2),  # Example 1. Positive step
        (10, -2, -2)  # Example 2. Negative step
    ]

    print("Results of custom vs. built-in range function:")
    for example_num, (start, stop, step) in enumerate(examples, start=1):
        # Print the example number
        print(f"Example {example_num}:")

        custom_range_results = list(my_range(start, stop, step))
        built_in_range_results = list(range(start, stop, step))

        for index, (custom_item, built_in_item) in enumerate(zip(custom_range_results, built_in_range_results), start=1):
            print(f" Number {index}: {custom_item} || {built_in_item}")

        print("-" * 80)  # Separator for readability


def task2():
    """Demonstrate a generator comprehension."""
    numbers_generator = (number for number in my_range(1,11))
    print("Generator that returns numbers from 1 to 10:")
    for number in numbers_generator:
        print(number)


# Main Flow. User to enter the task number
task_number = input("Please select a task, 1 or 2: ")

# Execute the corresponding task or notify the user of invalid input
match task_number:
    case '1':
        task1()
    case '2':
        task2()
    case _:
        print("Invalid input. Please enter 1 or 2.")
