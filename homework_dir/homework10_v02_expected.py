""" Homework 10. Decorators """
import time


def time_decorator(func):
    """Decorator to measure and report the execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"{func.__name__} function is executed in {duration: .4f} seconds.")
        return result
    return wrapper


@time_decorator
def sum_of_squares(n: int) -> None:
    """Calculates the sum of squares of all integers from 0 up to n."""
    result = sum(i ** 2 for i in range(1, n + 1))
    return print(f"The sum of squares up to {n} is: {result}")


@time_decorator
def sum_of_even_numbers(n: int) -> None:
    """Calculates the sum of even numbers from 0 up to n."""
    result = sum(i for i in range(0, n + 1) if i % 2 == 0)
    print(f"The sum of even numbers up to {n} is: {result}")


@time_decorator
def sum_of_odd_numbers(n: int) -> None:
    """Calculates the sum of odd numbers from 0 up to n."""
    result = sum(i for i in range(0, n + 1) if i % 2 != 0)
    print(f"The sum of odd numbers up to {n} is: {result}")


def task1():
    """Demonstrates the use of the time decorator."""
    num = int(input("Enter a positive integer number: "))
    sum_of_squares(num)
    sum_of_even_numbers(num)
    sum_of_odd_numbers(num)


def logger(prefix: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} function {prefix}.")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@logger('adds two numbers')
def add(x, y):
    return print(f"The sum of {x} and {y} is: {x + y}")


@logger('subtracts the second number from the first')
def subtract(x, y):
    return print(f"The difference between {x} and {y} is: {x - y}")


@logger('multiplies two numbers')
def multiply(x, y):
    return print(f"The product of {x} and {y} is: {x * y}")


@logger('divides the first number by the second')
def divide(x, y):
    if y == 0:
        return print("Error: Division by zero is not allowed.")
    return print(f"The division of {x} by {y} is: {x / y}")


def task2():
    """Demonstrates the use of the decorator with argument."""
    add(5.5, 3.3)
    subtract(-10, -5)
    multiply(4, 3)
    divide(20, 4)
    divide(10, 0)


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
