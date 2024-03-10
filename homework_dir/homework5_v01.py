""" Homework 5 """


class NegativeNumberError(Exception):
    """Exception raised for errors in the input if the number is negative."""
    pass


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
        user_input1 = input("Enter the 1st number: ")
        if user_input1.lower() == 'q':
            break  # Exit the loop and end the program
        user_input2 = input("Enter the 2nd number: ")

        try:
            # Attempt to convert inputs to a float
            num1 = float(user_input1)
            num2 = float(user_input2)

            # User to enter an operation
            op = input("Enter the operation (+, -, *, /): ")

            # Arithmetic operations
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
                        raise ZeroDivisionError("Error: Cannot divide by zero. Please enter a divisor other than 0.")
                    result = num1 / num2
                case _:
                    print("Invalid operation. Please choose from +, -, *, /.")
                    continue  # Skip the rest of the loop and prompt for inputs again

        # Exceptions handling
        except ValueError as ve:
            print(f"{str(ve).capitalize()}. Please enter a valid number.")
        except ZeroDivisionError as zde:
            print(zde)

        # This block is executed if no exceptions were raised in the try block
        else:
            print("The result is:", result)

        # End of calculation
        finally:
            print("Operation completed. You can continue or enter 'q' for the 1st prompt to quit.")

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
