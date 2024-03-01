""" Homework 3 """


def task1():
    # Print intro
    task1_intro = 'Check if a Word is a Palindrome'.center(50)
    print(task1_intro)

    # User input
    user_input = input("Enter a word: ")

    # Converting to lower case to ensure the comparison is case-insensitive
    user_input = user_input.lower()

    # Checking if the word is equal to its reverse using reversed() function and join() method
    result_str_method = ''.join(reversed(user_input))

    # Checking if the word is equal to its reverse using slicing
    result_slicing = user_input[::-1]

    # Output the result
    print("Using String Methods:", '+' if result_str_method == user_input else '-')
    print("Using Slicing:", '+' if result_slicing == user_input else '-')


# User to enter the task number
task_number = input("Enter the task number (1, 2, 3, or 4): ")

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
    case _:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
