import pytest
from homework_dir.lesson16_pytest_fixtures.src.store.store_facade import StoreFacade


@pytest.fixture(scope='package', autouse=True)
def global_setup():
    """
    Sets up a configuration that is automatically used across all tests in a package.

    Yields:
        dict: A configuration dictionary that could be modified by tests.
    Teardown after all tests in the package have run.
    """
    config = {'parameter': 'value'}
    print("Global setup for package")
    yield config
    print("Teardown global setup")


@pytest.fixture(name='store')
def store_facade(request):
    """
    Provides a fresh instance of StoreFacade for each test that requires it.

    Yields:
        StoreFacade: An instance to be used in tests.
    Cleans up by clearing the catalog to ensure a clean state for subsequent tests.
    """
    print(f"Setting up StoreFacade instance for the test")
    store = StoreFacade()
    yield store
    print(f"Cleaning up StoreFacade instance for the test")
    del store.catalog.phones


@pytest.fixture(name='store_with_param', scope='class')
def store_facade_to_work_with_catalog(request):
    """
    Provides a StoreFacade instance configured with optional initial phone data.

    This fixture initializes the StoreFacade with a phone if provided in 'request.param'.

    Yields:
        tuple: The StoreFacade instance and the description of the first phone in the catalog.
    Cleans up by clearing the catalog to ensure a clean state for subsequent tests.
    """
    print(f"Setting up StoreFacade instance for the test")
    store = StoreFacade()
    phone_info = request.param
    if phone_info:
        store.add_phone_to_catalog(*phone_info)
    yield store, str(store.show_catalog()[0])
    print(f"Cleaning up StoreFacade instance for the test")
    del store.catalog.phones


@pytest.fixture(name='pre_filled_store', scope='class')
def setup_store_with_phones():
    """
    Initializes a StoreFacade instance with a predefined set of phones.

    Useful for testing functionality that requires existing catalog entries.

    Yields:
        StoreFacade: An instance pre-filled with several phone models and their prices.
    Cleans up by clearing the catalog to ensure a clean state for subsequent tests.
    """
    store = StoreFacade()
    phones = [
        ('iPhone 12', 999),
        ('Samsung Galaxy S20', 850),
        ('Google Pixel 5', 700)
    ]
    for model, price in phones:
        store.add_phone_to_catalog(model, price)

    print(f"Store setup with {len(phones)} phones.")
    yield store
    del store.catalog.phones
    print("Store catalog cleared.")