import csv
import random


def load_data_from_csv(file_path: str) -> list:
    """Load all rows from a CSV file into a list of dictionaries."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


def select_random_data(file_path: str) -> dict:
    """Randomly select one row from the CSV data."""
    data = load_data_from_csv(file_path)
    return random.choice(data)
