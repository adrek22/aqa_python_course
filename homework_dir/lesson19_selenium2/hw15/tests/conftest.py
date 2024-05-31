import allure
import pytest
from homework_dir.lesson19_selenium2.hw15 import config
from homework_dir.lesson19_selenium2.hw15.utils.driver_factory import driver_factory

_driver_instance = None  # Global variable to keep track of the driver instance


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
    global _driver_instance
    browser = pytestconfig.getoption('browser')
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.get(config.browser.base_url)
    _driver_instance = driver

    yield driver

    driver.quit()
    _driver_instance = None


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
    global _driver_instance
    if _driver_instance:
        try:
            screenshot = _driver_instance.get_screenshot_as_png()

            test_name = node.name
            test_location = f"File: {node.fspath}, Line: {node.location[1]}, Function: {node.location[2]}"
            failure_reason = report.longreprtext

            exception_info = call.excinfo
            exception_type = exception_info.typename if exception_info else 'Unknown'
            exception_value = str(exception_info.value) if exception_info else 'No exception value'

            allure.attach(
                screenshot,
                name=(
                    f"Screenshot for {test_name} due to found {exception_type}: {exception_value}"
                ),
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                test_location,
                name='Location',
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                failure_reason,
                name=f'Failure reason',
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
