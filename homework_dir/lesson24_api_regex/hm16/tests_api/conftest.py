import random

import allure
import pytest
from homework_dir.lesson24_api_regex.hm16.backend.pets_interface import pet_api


@allure.title("Generates a random pet ID for testing")
@pytest.fixture(name="random_pet_id")
def generate_random_pet_id():
    random_id = random.randint(0, 999)
    print(f"\nGenerated Random Pet ID: {random_id}")
    return random_id


@allure.title("Creates a pet with the given random ID and returns the response JSON.")
@pytest.fixture()
def add_pet(random_pet_id):
    payload = {
        "id": random_pet_id,
        "category": {
            "id": 1,
            "name": "category_name"
        },
        "name": "pet_name",
        "photoUrls": [
            "url_1",
            "url_n"
        ],
        "tags": [
            {
                "id": 1,
                "name": "tag_1_name"
            },
            {
                "id": 999,
                "name": "tag_n_name"
            }
        ],
        "status": "available|pending|sold"
    }
    response = pet_api.create_pet(payload=payload)
    return response.json()


@allure.title("Deletes the pet with the given random ID after the test is done.")
@pytest.fixture
def clean_up_pet(random_pet_id):
    yield
    pet_api.delete_pet(pet_id=random_pet_id)
