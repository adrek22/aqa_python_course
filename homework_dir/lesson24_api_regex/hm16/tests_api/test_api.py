import allure
from homework_dir.lesson24_api_regex.hm16.backend import schemas
from homework_dir.lesson24_api_regex.hm16.backend.pets_interface import pet_api
from homework_dir.lesson24_api_regex.hm16.backend.schema_validation import validate_schema


@allure.title("Add a new pet")
@allure.description("Test adding a new pet and validate the response against the schema.")
@allure.tag("API", "Pets")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("assignee", "Mykhailo")
@allure.link("https://petstore.swagger.io/", name="API Documentation")
@allure.testcase("API-101")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Create Pet")
@allure.feature("Add Pet")
def test_add_new_pet(random_pet_id, clean_up_pet):
    payload = {
        "id": random_pet_id,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Max",
        "photoUrls": [
            "https://example.com/photos/max1.jpg",
            "https://example.com/photos/max2.jpg"
        ],
        "tags": [
            {
                "id": 101,
                "name": "Friendly"
            },
            {
                "id": 102,
                "name": "Playful"
            }
        ],
        "status": "available"
    }
    with allure.step("Step 1. Create pet with payload"):
        response = pet_api.create_pet(payload=payload)
    response_json = response.json()
    with allure.step("Step 2. Assert response reason"):
        assert response.reason == 'OK', f"Expected reason: OK, actual {response.reason}"
    with allure.step("Step 3. Assert id in response"):
        assert response_json['id'] == random_pet_id, f"Expected id: {random_pet_id}, actual {response_json['id']}"
    with allure.step("Step 4. Validate response against schema"):
        validate_schema(response.json(), schemas.ADD_PET)


@allure.title("Create a pet with invalid input")
@allure.description("Test creating a pet with invalid input and validate the response against the error schema.")
@allure.tag("API", "Pets", "Negative")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("assignee", "Mykhailo")
@allure.testcase("API-102")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Create Pet")
@allure.feature("Create Pet with Invalid Input")
def test_create_pet_with_invalid_input():
    payload = {
        "id": "a1",  # invalid type
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Max",
        "photoUrls": [
            "https://example.com/photos/max1.jpg",
            "https://example.com/photos/max2.jpg"
        ],
        "tags": [
            {
                "id": 101,
                "name": "Friendly"
            },
            {
                "id": 102,
                "name": "Playful"
            }
        ],
        "status": "available"
    }
    response = pet_api.create_pet(payload=payload, negative_flow=True)
    assert response.status_code == 405, f"Expected: 405 status, actual: {response.status_code}"
    assert response.reason == 'Invalid input', f"Expected reason: Invalid input, actual {response.reason}"
    validate_schema(response.json(), schemas.ERROR)


@allure.title("Update an existing pet")
@allure.description("Test updating an existing pet and validate the response against the schema.")
@allure.tag("API", "Pets")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("assignee", "Mykhailo")
@allure.link("https://petstore.swagger.io/", name="API Documentation")
@allure.testcase("API-103")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Update Pet")
@allure.feature("Update Pet")
def test_update_existing_pet(random_pet_id, add_pet, clean_up_pet):
    payload = {
        "id": random_pet_id,
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "name": "Whiskers",
        "photoUrls": [
            "https://example.com/photos/whiskers1.jpg",
            "https://example.com/photos/whiskers2.jpg"
        ],
        "tags": [
            {
                "id": 201,
                "name": "Independent"
            },
            {
                "id": 202,
                "name": "Curious"
            }
        ],
        "status": "pending"
    }
    response = pet_api.update_pet(payload=payload)
    response_json = response.json()
    assert response.reason == 'OK', f"Expected reason: OK, actual {response.reason}"
    assert response_json['id'] == random_pet_id, f"Expected id: {random_pet_id}, actual {response_json['id']}"
    validate_schema(response.json(), schemas.ADD_PET)


@allure.title("Update pet with invalid ID")
@allure.description("Test updating a pet with an invalid ID and validate the response against the error schema.")
@allure.tag("API", "Pets", "Negative")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("assignee", "Mykhailo")
@allure.testcase("API-104")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Update Pet")
@allure.feature("Update Pet with Invalid ID")
def test_update_pet_with_invalid_id(add_pet, clean_up_pet):
    payload = {
        "id": 1234567890,  # invalid id
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "name": "Whiskers",
        "photoUrls": [
            "https://example.com/photos/whiskers1.jpg",
            "https://example.com/photos/whiskers2.jpg"
        ],
        "tags": [
            {
                "id": 201,
                "name": "Independent"
            },
            {
                "id": 202,
                "name": "Curious"
            }
        ],
        "status": "pending"
    }
    response = pet_api.update_pet(payload=payload, negative_flow=True)
    assert response.status_code == 400, f"Expected: 400 status, actual: {response.status_code}"
    assert response.reason == 'Invalid ID supplied', f"Expected reason: Invalid ID supplied, actual {response.reason}"
    validate_schema(response.json(), schemas.ERROR)


@allure.title("Find a pet by ID")
@allure.description("Test finding a pet by ID and validate the response against the schema.")
@allure.tag("API", "Pets")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("assignee", "Mykhailo")
@allure.link("https://petstore.swagger.io/", name="API Documentation")
@allure.testcase("API-105")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Find Pet")
@allure.feature("Find Pet")
def test_find_pet_by_id(add_pet, clean_up_pet):
    created_id = add_pet['id']
    response = pet_api.find_pet_by_id(pet_id=created_id)
    response_json = response.json()
    assert response.reason == 'OK', f"Expected reason: OK, actual {response.reason}"
    assert response_json['id'] == created_id, f"Expected id: {created_id}, actual {response_json['id']}"
    validate_schema(response.json(), schemas.GET_PET)


@allure.title("Delete a pet")
@allure.description("Test deleting a pet and validate the response against the schema.")
@allure.tag("API", "Pets")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("assignee", "Mykhailo")
@allure.link("https://petstore.swagger.io/", name="API Documentation")
@allure.testcase("API-106")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Delete Pet")
@allure.feature("Delete Pet")
def test_delete_pet(add_pet):
    created_id = add_pet['id']
    response = pet_api.delete_pet(pet_id=created_id)
    response_json = response.json()
    assert response.reason == 'OK', f"Expected reason: OK, actual {response.reason}"
    assert response_json['message'] == str(created_id), f"Expected deletion message to be {created_id} but got {response_json['message']}"
    validate_schema(response.json(), schemas.DELETE_PET)


@allure.title("Find a deleted pet")
@allure.description("Test finding a deleted pet and expect a 404 status code.")
@allure.tag("API", "Pets", "Negative")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("assignee", "Mykhailo")
@allure.link("https://petstore.swagger.io/", name="API Documentation")
@allure.testcase("API-107")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Find Pet")
@allure.feature("Find Deleted Pet")
def test_find_deleted_pet(add_pet):
    created_id = add_pet['id']
    pet_api.delete_pet(pet_id=created_id)
    response = pet_api.find_pet_by_id(pet_id=created_id, negative_flow=True)
    response_json = response.json()
    assert response.status_code == 404, f"Expected 404 status for deleted pet but got {response.status_code}"
    assert response.reason == 'Not Found', f"Expected reason: OK, actual {response.reason}"
    assert response_json['type'] == 'error', f"Expected type: error, actual: {response_json['type']}"
    assert response_json['message'] == 'Pet not found', f"Expected message: Pet not found, actual: {response_json['message']}"
    validate_schema(response.json(), schemas.ERROR)


@allure.title("Pet not found for deleting")
@allure.description("Test attempting to delete a non-existent pet and validate the response against the error schema.")
@allure.tag("API", "Pets", "Negative")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("assignee", "Mykhailo")
@allure.testcase("API-108")
@allure.parent_suite("API Tests")
@allure.suite("Pets API")
@allure.sub_suite("Delete Pet")
@allure.feature("Delete Non-existent Pet")
def test_pet_not_found_for_deleting(add_pet, clean_up_pet):
    response = pet_api.delete_pet(pet_id=add_pet['id']+1, negative_flow=True)
    assert response.status_code == 404, f"Failed to delete pet: {response.text}"
    assert response.reason == 'Not Found', f"Expected reason: OK, actual {response.reason}"
