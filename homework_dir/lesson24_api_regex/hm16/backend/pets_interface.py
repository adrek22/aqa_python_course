import allure

from homework_dir.lesson24_api_regex.hm16.backend.api_interface import APIInterface


class PetsInterface(APIInterface):
    """Interface for interacting with the Pets section of the API."""
    def create_pet(self, payload: dict, **kwargs):
        """Create a new pet record."""
        with allure.step("Create pet with a payload"):
            return self._post('pet', json=payload, **kwargs)

    def update_pet(self, payload: dict, **kwargs):
        """Update an existing pet record."""
        return self._put('pet', body=payload, **kwargs)

    def delete_pet(self, pet_id: int, **kwargs):
        """Delete a pet record by its ID."""
        return self._delete(f'pet/{pet_id}', **kwargs)

    def find_pet_by_id(self, pet_id: int, **kwargs):
        """Retrieve a pet's details by its ID."""
        return self._get(f'pet/{pet_id}', **kwargs)


pet_api = PetsInterface()
