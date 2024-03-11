""" Homework 5 """


class NegativeNumberError(Exception):
    """Exception raised for errors in the input if the number is negative."""
    pass


def get_number_or_q_input(prompt):
    """Prompts the user for a number or 'q' to quit, ensuring the input is converted to a float."""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            return 'q'  # Indicate the desire to exit
        try:
            return float(user_input)  # Successfully return the float conversion
        except ValueError as ve:
            print(f"{str(ve).capitalize()}. Please enter a valid number or 'q' to quit.")


def get_operation_input(prompt):
    """Prompts the user for an operation or 'q' to quit, ensuring the valid operation is entered."""
    while True:
        user_input = input(prompt)
        # Handle operation input
        try:
            if user_input not in ['+', '-', '*', '/']:
                raise Exception("Invalid operation. Please choose from +, -, *, /.")
            return user_input
        # Exceptions handling
        except Exception as e:
            print(e)


def task1():
    try:
        # Ask the user for a number
        number = float(input("Enter a number: "))

        # Check for positive input
        if number < 0:
            raise NegativeNumberError("Cannot calculate the square root of a negative number.")

    # Handle the exception for negative inputs
    except NegativeNumberError as nne:
        print(nne)

    # Calculate the square root if no exception was raised
    else:
        square_root = number ** 0.5
        # Print the results with rounded numbers
        print(f"The square root of {number} is: {round(square_root, 4)}")

    # End of calculation
    finally:
        print("Completion of the calculation operation.")


def task2():
    try:
        # Ask the user for a number
        number = float(input("Enter a number: "))

        # Check for negative input
        if number < 0:
            raise NegativeNumberError("Cannot calculate the square root of a negative number.")

    # Handle the exception for not number and for negative inputs
    except ValueError as ve:
        print(f"{str(ve).capitalize()}. Please enter a valid number.")
    except NegativeNumberError as nne:
        print(nne)

    # Calculate the square root if no exception was raised
    else:
        square_root = number ** 0.5
        # Print the results with rounded numbers
        print(f"The square root of {number} is: {round(square_root, 4)}")

    # End of calculation
    finally:
        print("Completion of the calculation operation.")


def task3():
    while True:
        # User to enter the 1st and 2nd number
        num1 = get_number_or_q_input("Enter the 1st number: ")
        if num1 == 'q':
            break  # Exit the loop if 'q' is entered

        num2 = get_number_or_q_input("Enter the 2nd number: ")
        if num2 == 'q':
            break  # Exit the loop if 'q' is entered

        # User to enter an operation
        op = get_operation_input("Enter the operation (+, -, *, /): ")

        try:
            # Arithmetic operations
            result = None
            match op:
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '*':
                    result = num1 * num2
                case '/':
                    # Check for division by zero
                    if num2 == 0:
                        raise ZeroDivisionError(
                            "Error: Cannot divide by zero. Please enter a divisor other than 0.")
                    result = num1 / num2

        # Exceptions handling
        except ZeroDivisionError as zde:
            print(zde)

        # This block is executed if no exceptions were raised in the try block
        else:
            print("The result is:", result)

        # End of calculation
        finally:
            print("Operation completed. You can continue or enter 'q' at any prompt to quit.")

    # Exit from loop
    print("Calculator has been exited. Thank you for using the calculator!")


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
