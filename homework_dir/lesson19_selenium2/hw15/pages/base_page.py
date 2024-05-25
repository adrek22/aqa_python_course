import os

from datetime import datetime
from abc import abstractmethod, ABC
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from homework_dir.lesson19_selenium2.hw15 import config


class BasePage(ABC):
    """
    Base class that all page models can extend to include all common
    elements and functionality for interaction with web pages.
    """
    timeout = config.browser.timeout

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        print('\nPage loaded:', self.title)

    @property
    @abstractmethod
    def title(self):
        """Mandatory title attribute for child classes."""
        pass

    @property
    def driver(self) -> WebDriver:
        """Provides access to the WebDriver instance."""
        return self.__driver

    @property
    def action_chains(self) -> ActionChains:
        """Provides access to ActionChains for performing complex user interactions."""
        return ActionChains(driver=self.driver)

    def wait_until(self, locator: tuple, condition, timeout: int = timeout, **kwargs) -> WebElement:
        """Wait for a certain condition to be true for an element before proceeding."""
        wait = WebDriverWait(self.driver, timeout, kwargs.get('poll_frequency', 0.5))
        return wait.until(condition(locator))

    def wait_until_not(self, locator: tuple, condition, timeout: int = timeout) -> WebElement:
        """Waits until a specific condition is not met for an element."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until_not(condition(locator))

    def scroll_into_view(self, element: WebElement) -> WebElement:
        """Scroll the web page to make an element visible."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def _wait_for_element_and_scroll(self, locator: tuple, **kwargs) -> WebElement:
        """Waits for an element to be visible and scrolls it into view, then returns the WebElement."""
        element = self.wait_until(locator, ec.visibility_of_element_located, kwargs=kwargs.get('poll_frequency', 0.5))
        self.scroll_into_view(element)
        return element

    def is_element_displayed(self, locator: tuple) -> bool:
        """Checks if an element is visible on the web page and returns a boolean."""
        try:
            element = self.wait_until(locator, ec.visibility_of_element_located)
            return element.is_displayed()
        except TimeoutException:
            return False

    def is_element_not_displayed(self, locator: tuple) -> bool:
        """Checks if an element is not visible on the web page and returns a boolean."""
        try:
            self.wait_until_not(locator, ec.visibility_of_element_located)
            return True
        except TimeoutException:
            return False

    def click(self, locator: tuple):
        """Click on an element identified by a locator after ensuring it is clickable and in view."""
        element = self.wait_until(locator, ec.element_to_be_clickable)
        self.scroll_into_view(element)
        element_text = self.get_element_text(locator)
        element.click()
        print(f'Web element with "{element_text}" text is clicked')

    def type(self, locator: tuple, text: str):
        """Sends keys to the element specified by locator after ensuring it is visible and in view."""
        element = self._wait_for_element_and_scroll(locator)
        element.clear()
        element.send_keys(text)
        element_text = self.get_element_by_attribute(locator, 'placeholder')
        print(f'{text} is typed into the "{element_text}" field')

    def hover_over(self, locator: tuple):
        """Hover over an element identified by a locator after ensuring it is visible and in view."""
        element = self._wait_for_element_and_scroll(locator)
        self.action_chains.move_to_element(element).perform()
        element_text = self.get_element_text(locator)
        print(f'Mouse is hovered over the "{element_text}" element')

    def get_css_property(self, locator: tuple, css_property: str) -> str:
        """Get css property of an element."""
        element = self.wait_until(locator, ec.presence_of_element_located)
        return element.value_of_css_property(css_property)

    def get_element_by_attribute(self, locator: tuple, attribute_name: str) -> str:
        """Get an attribute value of an element."""
        element = self._wait_for_element_and_scroll(locator)
        return element.get_attribute(attribute_name)

    def get_element_text(self, locator: tuple) -> str:
        """Get the visible text of an element."""
        element = self._wait_for_element_and_scroll(locator)
        return element.text

    def check_elements_number(self, locator: tuple, expected_number: int) -> bool:
        """Counts the elements matched by the specified locator and compares with expected number"""
        self.wait_until(locator, ec.presence_of_all_elements_located)
        elements = self.driver.find_elements(locator)
        actual_number = len(elements)
        return actual_number == expected_number

    def check_element_attribute(self, locator: tuple, attribute_name: str, expected_value: str) -> bool:
        """Verifies that value of a specified attribute of a specified element matches the expected value."""
        element = self._wait_for_element_and_scroll(locator)
        actual_value = element.get_attribute(attribute_name)
        return actual_value == expected_value

    @staticmethod
    def timestamp_as_identification() -> str:
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")
        return date_time

    def screenshot(self, name=''):
        """Define a method to take a screenshot of the current page"""
        class_name = self.__class__.__name__
        directory = os.path.join(os.getcwd(), 'screenshots')

        # Ensure the screenshots directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Define the file path for the screenshot
        filename = f"{name}{class_name}_{self.timestamp_as_identification()}.png"
        file_path = os.path.join(directory, filename)

        # Save the screenshot
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved to {file_path}")

    @staticmethod
    def soft_assert(field_checks):
        """Performs soft assertions on a collection of conditions
        and accumulates errors without stopping the test execution."""
        errors = []
        for description, (condition_method, error_message) in field_checks.items():
            result = condition_method
            if not result:
                errors.append(error_message)
            else:
                print(f"Assertion passed: {description}")

        if errors:
            error_messages = "\n".join(errors)
            raise AssertionError(f"Encountered errors in form validation:\n{error_messages}")

    # Define context manager methods for entering and exiting the context
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'The "{self.title}" page is verified')
        # self.screenshot()
