""" Homework 2 """

# User to enter the task number
task_number = input("Enter the task number (1, 2, or 3): ")

# Execute the corresponding task or notify the user of invalid input
match task_number:
    case '1':
        """ Task 1 """

        # User to enter the temperature in Celsius
        task1_user_input = input("Enter the temperature in degrees Celsius: ")

        try:
            # Attempt to convert the input to a float
            celsius_input = float(task1_user_input)

            # Convert Celsius to Fahrenheit
            fahrenheit = round(celsius_input * 9 / 5 + 32, 2)

            # Convert Celsius to Kelvin
            kelvin = round(celsius_input + 273.15, 2)

            # Print the results with rounded numbers and converted to strings
            print(celsius_input, "C is equivalent to ", fahrenheit, "F and ", kelvin, "K.", sep='')
        except ValueError:
            # If conversion to float fails, inform the user.
            print("Not number is entered. Please enter a valid number.")
    case '2':
        """ Task 2 """

        # User to enter the 1st and 2nd water volume and temperature
        v1_input = input("Enter the 1st water volume in liters: ")
        t1_input = input("Enter the 1st water temperature in Celsius: ")
        v2_input = input("Enter the 2nd water volume in liters: ")
        t2_input = input("Enter the 2nd water temperature in Celsius: ")

        try:
            # Attempt to convert the input to a float
            v1 = float(v1_input)
            t1 = float(t1_input)
            v2 = float(v2_input)
            t2 = float(t2_input)

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

                # Display the results, converting to int if the value is a whole number
                if total_volume == int(total_volume):
                    total_volume = int(total_volume)
                if mixture_temperature == int(mixture_temperature):
                    mixture_temperature = int(mixture_temperature)
                print("The total volume of the mixture is: ", total_volume, "l.", sep='')
                print("The temperature of the mixture is: ", mixture_temperature, "C.", sep='')
        except ValueError:
            # If conversion to float fails, inform the user.
            print("Not number is entered. Please enter a valid number for volume and temperature.")
    case '3':
        """ Task 3 """

        # User to enter the 1st and 2nd number
        task3_user_input1_num1 = input("Enter the 1st number: ")
        task3_user_input2_op = input("Enter the operation (+, -, *, /): ")
        task3_user_input3_num2 = input("Enter the 2nd number: ")

        # Try to convert inputs into int, then float, else error
        try:
            num1 = int(task3_user_input1_num1)
        except ValueError:
            try:
                num1 = float(task3_user_input1_num1)
            except ValueError:
                print("Invalid number. Please enter the 1st valid number.")
        try:
            num2 = int(task3_user_input3_num2)
        except ValueError:
            try:
                num2 = float(task3_user_input3_num2)
            except ValueError:
                print("Invalid number. Please enter the 1st valid number.")

        match task3_user_input2_op:
            case '+':
                result = num1 + num2
                print("The result is", result)
            case '-':
                result = num1 - num2
                print("The result is", result)
            case '*':
                result = num1 * num2
                print("The result is", result)
            case '/':
                # Check for division by zero
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print("The result is", result)
            case _:
                print("Invalid operation. Please enter one of the following: +, -, *, /.")
    case _:
        print("Invalid input. Please enter 1, 2, or 3.")
