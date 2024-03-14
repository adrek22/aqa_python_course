""" Homework 6 """


def sum_range(start: int, end: int) -> int:
    # Ensure start is not greater than end
    if start > end:
        start, end = end, start  # Swap values

    # Calculate the sum of the range
    sum_of_int = sum(range(start, end + 1))
    return sum_of_int


def task1():
    # User to enter start and end numbers
    start_num = int(input("Enter the start number as int: "))
    end_num = int(input("Enter the emd number as int: "))

    # Print the results
    print(f"The sum of all integers from {start_num} to {end_num} is: {sum_range(start_num, end_num)}")


def square(side: float) -> tuple:
    perimeter = side * 4  # The perimeter of a square is 4 times its side
    area = side ** 2  # The area of a square is side squared
    diagonal = side * (2 ** 0.5)  # The diagonal using the Pythagorean theorem
    return perimeter, area, diagonal


def task2():
    side_length = float(input("Enter the side length of the square: "))
    perimeter, area, diagonal = square(side_length)

    # Print the results
    print(f"Given the side of the square as {side_length}:")
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Diagonal: {diagonal:.2f}")


def get_user_input() -> str:
    return input("Enter your data (list, tuple, dict, int): ")


def process_input(user_input: str):
    try:
        # Attempt to convert input based on leading characters
        if user_input.startswith("[") and user_input.endswith("]"):
            # Likely a list
            data_type = "list"
        elif user_input.startswith("(") and user_input.endswith(")"):
            # Likely a tuple
            data_type = "tuple"
        elif user_input == '{}' or user_input.startswith("{") and user_input.endswith("}") and ':' in user_input:
            # Likely a dict
            data_type = "dict"
        elif user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            # Likely an int, considering negative integers as well
            data_type = "int"
        else:
            raise ValueError("Unknown data type.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"User is going to work with {data_type}.")


# Main Flow. User to enter the task number
task_number = input("Please select a task from 1 to 3: ")

# Execute the corresponding task or notify the user of invalid input
match task_number:
    case '1':
        task1()
    case '2':
        task2()
    case '3':
        process_input(get_user_input())
    case _:
        print("Invalid input. Please enter 1, 2, or 3.")
