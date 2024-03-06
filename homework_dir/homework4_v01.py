""" Homework 4 """


def task1():
    # Print intro
    print('Task 1: Capitalize List Of Names'.center(50))

    # Initial list of names
    lowercase_names = ["john", "marta", "james", "amanda", "marianna"]

    # Convert each name in the list to start with a capital letter
    capitalized_names = [name.title() for name in lowercase_names]

    # Print the result
    print("Initial list: ", lowercase_names, "\nResult list: ", capitalized_names)


def task2():
    # Print intro
    print("Task 2: Camel Case to snake_case".center(50))

    # Initial CamelCase variables
    camel_case_variables = ["FirstItem", "FriendsList", "MyTuple"]

    # Method 1: Convert variables to snake_case using iterative approach
    snake_case_variables1 = []
    for var in camel_case_variables:
        snake_case_name = var[0].lower()  # Start with the first letter in lowercase
        for char in var[1:]:
            if char.isupper():
                snake_case_name += '_' + char.lower()  # Add '_' before an uppercase letter and convert it to lowercase
            else:
                snake_case_name += char  # Add the character as is
        snake_case_variables1.append(snake_case_name)

    # Method 2: Convert variables to snake_case using combined 2 list comprehension
    snake_case_variables2 = [
        ''.join(['_' + c.lower() if c.isupper() else c for c in var]).lstrip('_')
        for var in camel_case_variables
    ]

    # Print the results
    print("Initial list: ", camel_case_variables)
    print("Method 1:", snake_case_variables1)
    print("Method 2:", snake_case_variables2)


def task3():
    # Print intro
    print('Task 3: Favorite Programming Languages'.center(50))

    # Creating the dictionary
    programming_languages = {
        'Python': 'Guido van Rossum',
        'JavaScript': 'Brendan Eich',
        'C++': 'Bjarne Stroustrup',
        'Java': 'James Gosling',
        'Ruby': 'Yukihiro Matsumoto'
    }
    print("Initial dictionary: ", programming_languages)

    # Print message for each language and its developer
    for lang, creator in programming_languages.items():
        print(f'My favorite programming language is {lang}. It was created by {creator}.')

    # Remove a pair amd display the updated dictionary
    programming_languages.popitem()
    print("\nThe final dictionary: ", programming_languages)


def task4():
    # Print intro
    print("Task 4: Print Only Names".center(50))

    # Initial list
    names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
    print("Initial list: ", names)

    # Iterate through the list and print only the names
    for name in names:
        # Skip any element that is not a string
        if not name == str(name):
            continue
        # Print the name
        print(name)


def task5():
    # Print intro
    print("Task 5: Print Only Int".center(50))

    # Initial list
    types = [1, 1000, 2, 12, {'key': 'value'}]
    print("Initial list: ", types)

    # Iterate through the list
    for value in types:
        # Check if the current item is of int type
        if type(value) == int:
            # Print the integer
            print(value)
        else:
            # Not int - print the message and stop the loop
            print(f"The loop does not work with \"{type(value).__name__}\" data type.")
            break


def task6():
    # Print intro
    print("Task 6: Count and Print Identical Symbols".center(50))

    # User input
    user_input = input("Enter a string: ")

    # Method 1: Count the symbols using get()
    char_counts_dict1 = {}
    # Iterate through each character in the user input
    for char in user_input:
        # Update the count for each character
        char_counts_dict1[char] = char_counts_dict1.get(char, 0) + 1

    # Method 2: Count the symbols using dict comprehension
    char_counts_dict2 = {symbol: user_input.count(symbol) for symbol in user_input}

    # Prepare and print the result using str.join() and Generator Expression
    print("Method 1:", ' '.join(f'{char},{count}' for char, count in char_counts_dict1.items()))
    print("Method 2:", ' '.join(f'{char},{count}' for char, count in char_counts_dict2.items()))


def task7():
    # Print intro
    print("Task 7: Updated Calculator. Note that invalid inputs are not processed except for division by 0.".center(50))

    for attempt in range(2):  # Control attempts with a for loop
        # User to enter of the 1st and 2nd number, and operator
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        op = input("Enter the operation (+, -, *, /): ")

        # Check for division by zero early for '/'
        if op == '/' and num2 == 0:
            print("Error: Cannot divide by zero.")
            if attempt == 0:  # First attempt
                print("You have 1 more try.")
                continue  # Give the user another attempt
            else:  # Second attempt
                print("You have no more tries left.")
                break  # Exit after the final attempt

        # Arithmetic operations if not division by zero
        match op:
            case '+':
                print("The result is", num1 + num2)
                break
            case '-':
                print("The result is", num1 - num2)
                break
            case '*':
                print("The result is", num1 * num2)
                break
            case '/':
                print("The result is", num1 / num2)
                break


# Main Flow. User to enter the task number
task_number = input("Enter the task number (1, 2, 3, 4, 5, 6, or 7): ")

# Execute the corresponding task or notify the user of invalid input
match task_number:
    case '1':
        task1()
    case '2':
        task2()
    case '3':
        task3()
    case '4':
        task4()
    case '5':
        task5()
    case '6':
        task6()
    case '7':
        task7()
    case _:
        print("Invalid input. Please enter 1, 2, 3, 4, 5, 6, or 7.")
