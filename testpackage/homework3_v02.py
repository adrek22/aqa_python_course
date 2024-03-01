""" Homework 3 """


def task1():
    # Print intro
    print('Task 1: Check if a Word is a Palindrome'.center(50))

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


def task2():
    # Print intro
    print("Task 2: Check if a Word is in the Text".center(50))

    # User input for the text and the word to search
    text_input = input("Enter the text: ")
    word_to_find = input("Enter the word to be found: ")

    # Convert both inputs to lower case to ensure the comparison is case-insensitive
    text_input = text_input.lower()
    word_to_find = word_to_find.lower()

    # Method 1: Using 'in' keyword
    method_in = "YES" if word_to_find in text_input else "NO"

    # Method 2: Using find() method
    method_find = "YES" if text_input.find(word_to_find) != -1 else "NO"

    # Method 3: Using count() method
    method_count = "YES" if text_input.count(word_to_find) > 0 else "NO"

    # Method 4: Using index() method with exception handling
    try:
        text_input.index(word_to_find)
        method_index = "YES"
    except ValueError:
        method_index = "NO"

    # Output the results
    print("Using 'in' keyword:", method_in)
    print("Using find() method:", method_find)
    print("Using count() method:", method_count)
    print("Using index() method:", method_index)


def task3():
    # Print intro
    print("Task 3: Email Validator".center(50))

    # User input for the email
    email_input = input("Enter the email to validate: ")

    # Method 1: Using 'in' keyword
    method_in = "YES" if '@' in email_input and '.' in email_input else "NO"

    # Method 2: Using find() method
    method_find = "YES" if email_input.find('@') != -1 and email_input.find('.') != -1 else "NO"

    # Method 3: Using count() method
    method_count = "YES" if email_input.count('@') > 0 and email_input.count('.') > 0 else "NO"

    # Method 4: Using index() method with exception handling
    try:
        email_input.index('@')
        email_input.index('.')
        method_index = "YES"
    except ValueError:
        method_index = "NO"

    # Output the results
    print("Using 'in' keyword:", method_in)
    print("Using find() method:", method_find)
    print("Using count() method:", method_count)
    print("Using index() method:", method_index)


def task4():
    # Print intro
    print("Task 4: Display Last Three Elements of List".center(50))

    # User input for the text
    text_input = input("Enter text separated by space: ")

    # Convert text to list
    text_list = text_input.split()

    # Check the number of spaces in the text
    num_spaces = text_input.count(' ')

    # Determine action based on the number of spaces
    if num_spaces < 2:
        print(f"The number of elements is less than 3. There are {num_spaces + 1} elements in the current list.")
    else:
        # Display the last 3 elements from the list
        print("The last three elements are:", text_list[-3:], "\nTotal elements:", num_spaces + 1)


# Main Flow. User to enter the task number
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
