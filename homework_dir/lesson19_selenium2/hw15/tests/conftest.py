import pytest
from homework_dir.lesson19_selenium2.hw15 import config
from homework_dir.lesson19_selenium2.hw15.utils.driver_factory import driver_factory


@pytest.fixture(scope='function')
def driver(pytestconfig):
    """
    A fixture to create and return a WebDriver instance based on the browser type provided via command-line option.
    It maximizes the window and navigates to the base URL specified in the configuration.
    The WebDriver instance is terminated at the end of each test to ensure a clean session.

    Args:
        pytestconfig (_pytest.config.Config): Pytest config object, automatically provided by pytest, used to access CLI options.

    Yields:
        webdriver: An instance of WebDriver initialized based on the specified browser and base URL.
    """
    browser = pytestconfig.getoption('browser')
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.get(config.browser.base_url)

    yield driver

    driver.quit()


def pytest_addoption(parser):
    """
    Defines command-line options for pytest.

    Args:
        parser (_pytest.config.argparsing.Parser): The parser for command-line options and ini-file values.
    """
    parser.addoption(
        '--browser',
        action='store',
        default=config.browser.type,
        help='Specify the browser to use for tests. Default is "chrome". Supports "chrome", "firefox", etc.'
    )
    # parser.addoption()
