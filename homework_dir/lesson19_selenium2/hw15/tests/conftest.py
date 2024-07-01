import logging
import allure
import pytest
from homework_dir.lesson19_selenium2.hw15 import config
from homework_dir.lesson19_selenium2.hw15.driver import shared_driver
from homework_dir.lesson19_selenium2.hw15.utils.driver_factory import driver_factory
from homework_dir.lesson19_selenium2.hw15.utils.environment_data_collection import generate_environment_properties
from homework_dir.lesson19_selenium2.hw15.utils.soft_step import ErrCatcher

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@allure.title("Create, return a WebDriver instance based on the browser type and terminate at the end of each test.")
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
    shared_driver.driver = driver
    version = driver.capabilities['browserVersion']
    generate_environment_properties(version)

    yield driver

    driver.quit()
    shared_driver.driver = None


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


def pytest_exception_interact(node, call, report):
    """
    Hook to interact with an exception raised during test execution.

    This function captures a screenshot when an exception occurs during a test,
    attaches it to the Allure report, and includes additional information about the test and the failure.

    Args:
        node (pytest.Item): The pytest test item.
        call (pytest.CallInfo): The test call information.
        report (pytest.TestReport): The test report generated after the test run.
    """
    if shared_driver.driver:
        try:
            test_name = node.name
            test_location = f"File: {node.fspath}, Line: {node.location[1]}, Function: {node.location[2]}"
            failure_reason = report.longreprtext

            exception_info = call.excinfo
            exception_type = exception_info.typename if exception_info else 'Unknown'
            exception_value = str(exception_info.value) if exception_info else 'No exception value'

            allure.attach(
                f"Exception type: {exception_type}\n"
                f"Exception value: {exception_value}"
                f"Location: {test_location}\n"
                f"Failure reason: {failure_reason}\n",
                name=(
                    f"Details for {test_name}"
                ),
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception as e:
            print(f"Error capturing screenshot: {e}")


@pytest.fixture(name='catcher')
def assertion_catcher():
    return ErrCatcher()
