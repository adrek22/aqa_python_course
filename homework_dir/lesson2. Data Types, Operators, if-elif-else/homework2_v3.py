""" Homework 2 """


def get_number_input(prompt):
    """ Prompts the user for a number, ensuring the input is converted to an int or float. """
    while True:
        user_input = input(prompt)
        try:
            # First, attempt to convert to an integer.
            return int(user_input)
        except ValueError:
            try:
                # If int conversion fails, try converting to a float.
                return float(user_input)
            except ValueError:
                # If both conversions fail, inform the user and repeat the prompt.
                print("Invalid input. Please enter a valid number.")


def to_int_if_int(number):
    """ Converts a number to an integer if it is integer"""
    if number == int(number):
        return int(number)
    else:
        return float(number)


def print_result(result):
    """ Prints the result """
    print("The result is", to_int_if_int(result))


def task1():
    """Converts temperature from Celsius to Fahrenheit and Kelvin."""
    # User to enter the temperature in Celsius
    celsius_input = get_number_input("Enter the temperature in degrees Celsius: ")

    # Convert Celsius to Fahrenheit
    fahrenheit = round(celsius_input * 9 / 5 + 32, 2)

    # Convert Celsius to Kelvin
    kelvin = round(celsius_input + 273.15, 2)

    # Print the results with rounded numbers
    print(celsius_input, "C is equivalent to ", fahrenheit, "F and ", kelvin, "K.", sep='')


def task2():
    """Calculates the mixture temperature and volume from 4 inputs."""
    # User to enter the 1st and 2nd water volume and temperature
    v1 = get_number_input("Enter the 1st water volume in liters: ")
    t1 = get_number_input("Enter the 1st water temperature in Celsius: ")
    v2 = get_number_input("Enter the 2nd water volume in liters: ")
    t2 = get_number_input("Enter the 2nd water temperature in Celsius: ")

    # Calculate the total volume of the mixture
    total_volume = v1 + v2

    # Ensure total volume is not 0 to avoid division by zero error
    if total_volume == 0:
        print("Cannot calculate the mixture temperature. Enter water volume > 0.")
    elif v1 < 0 or v2 < 0:
        print("Volume cannot be a negative number. Enter water volume > 0.")
    else:
        # Calculate the temperature of the resulting mixture
        mixture_temperature = round((v1 * t1 + v2 * t2) / total_volume, 2)

        # Convert to int if whole numbers
        total_volume = to_int_if_int(total_volume)
        mixture_temperature = to_int_if_int(mixture_temperature)

        # Display the results
        print("The total volume of the mixture is: ", total_volume, "l.", sep='')
        print("The temperature of the mixture is: ", mixture_temperature, "C.", sep='')


def task3():
    """Performs a basic arithmetic operation between two numbers."""
    # User to enter the 1st and 2nd number
    num1 = get_number_input("Enter the 1st number: ")
    num2 = get_number_input("Enter the 2nd number: ")

    # User to enter the operation
    task3_user_input2_op = input("Enter the operation (+, -, *, /): ")

    # Exit if no operation
    if task3_user_input2_op not in ['+', '-', '*', '/']:
        print("Invalid operation. Please enter one of the following: +, -, *, /.")
        return

    # Arithmetic operations
    match task3_user_input2_op:
        case '+':
            print_result(num1 + num2)
        case '-':
            print_result(num1 - num2)
        case '*':
            print_result(num1 * num2)
        case '/':
            # Check for division by zero
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print_result(num1 / num2)


# User to enter the task number
task_number = input("Enter the task number (1, 2, or 3): ")

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
