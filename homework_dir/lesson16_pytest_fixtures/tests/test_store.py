import pytest


@pytest.mark.positive
@pytest.mark.store
def test_catalog_empty_initially(store):
    """Verify that the catalog is empty upon initialization of the StoreFacade."""
    catalog = store.show_catalog()
    assert not catalog, "Catalog should be initially empty"


@pytest.mark.negative
@pytest.mark.store
@pytest.mark.skip("Not yet supported or implemented")
def test_add_phone_with_invalid_data(store):
    """Verify that the system rejects adding a phone with invalid data, like an empty model name or negative price."""
    try:
        store.add_phone_to_catalog('', -100)
        assert False, "Should not successfully add a phone with empty model name and negative price"
    except ValueError as e:
        assert str(e) == "Invalid model name or price", "Exception message should indicate invalid input"
    catalog = store.show_catalog()
    assert not catalog, "Catalog should remain empty after attempting to add invalid data"


@pytest.mark.positive
@pytest.mark.store_with_params
@pytest.mark.parametrize('store_with_param', [('iPhone', 1000), ('Samsung', 800)], indirect=True)
def test_catalog_contains_parametrized_phone(store_with_param):
    """Verify that the catalog accurately reflects phones added in a parametrized test setup."""
    store_instance, phone_description = store_with_param
    catalog = store_instance.show_catalog()
    assert catalog, "Catalog should not be empty"
    assert isinstance(catalog, list), "Catalog should be a list"
    assert phone_description == str(catalog[0]), f"Expected {phone_description} in catalog"


@pytest.mark.positive
@pytest.mark.store_with_params
@pytest.mark.parametrize('store_with_param', [('Pixel', 1200)], indirect=True)
def test_remove_phone(store_with_param):
    """Verify that the catalog is empty after the phone is removed, confirming removal functionality."""
    store_instance, _ = store_with_param
    store_instance.remove_phone_from_catalog('Pixel')
    catalog = store_instance.show_catalog()
    assert not catalog, "Catalog should be empty after removing the phone"


@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.store_with_params
@pytest.mark.parametrize('store_with_param', [('OnePlus', 950)], indirect=True)
def test_error_removing_non_existent_phone(store_with_param):
    """
    Verify the behavior of attempting to remove a phone that does not exist in the catalog.
    Expects a specific failure (None return or error handling), illustrating robustness against invalid operations.
    """
    store_instance, _ = store_with_param
    try:
        result = store_instance.remove_phone_from_catalog('Pixel')
        assert result is None, "Should return None for non-existent phone removal"
    except IndexError:
        print("Caught an IndexError when trying to remove a non-existent phone.")
    catalog = store_instance.show_catalog()
    assert len(catalog) == 1, "Catalog should still contain one phone"
    assert catalog[0].model == 'OnePlus', "Catalog should contain the OnePlus phone"


@pytest.mark.positive
@pytest.mark.pre_filled_store
def test_catalog_contains_all_initial_phones(pre_filled_store):
    """Verify that all predefined phones are present in the catalog."""
    catalog = pre_filled_store.show_catalog()
    expected_models = ['iPhone 12', 'Samsung Galaxy S20', 'Google Pixel 5']
    catalog_models = [phone.model for phone in catalog]
    assert all(model in catalog_models for model in expected_models), "All initial phones should be in the catalog."


@pytest.mark.positive
@pytest.mark.pre_filled_store
def test_remove_phone_from_pre_filled_catalog(pre_filled_store):
    """Verify that a specific phone can be removed from a catalog that was pre-filled with multiple phones."""
    pre_filled_store.remove_phone_from_catalog('Samsung Galaxy S20')
    catalog = pre_filled_store.show_catalog()
    assert not any(phone.model == 'Samsung Galaxy S20' for phone in catalog), "Samsung Galaxy S20 should be removed from the catalog."


@pytest.mark.positive
@pytest.mark.pre_filled_store
def test_catalog_length_after_removal(pre_filled_store):
    """Verify that the catalog length decreases appropriately, reflecting the removal accurately."""
    pre_filled_store.remove_phone_from_catalog('Google Pixel 5')
    catalog = pre_filled_store.show_catalog()
    assert len(catalog) == 2, "Catalog should contain exactly two phones after one removal."

