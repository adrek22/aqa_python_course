from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from homework_dir.lesson19_selenium2.hw15 import config
from homework_dir.lesson19_selenium2.hw15.locators import a1_home_page


class BasePage:
    """
    Base class that all page models can extend to include all common
    elements and functionality for interaction with web pages.
    """
    timeout = config.browser.timeout

    def __init__(self, driver: WebDriver):
        self.__driver = driver
    #     self._wait_for_page_load()
    #
    # def _wait_for_page_load(self):
    #     """Wait for the page to be loaded based on page body availability."""
    #     wait = WebDriverWait(self.driver, config.browser.timeout)
    #     wait.until(ec.presence_of_element_located(a1_home_page.body_tag))

    @property
    def driver(self) -> WebDriver:
        """Provides access to the WebDriver instance."""
        return self.__driver

    @property
    def action_chains(self) -> ActionChains:
        """Provides access to ActionChains for performing complex user interactions."""
        return ActionChains(driver=self.driver)

    def wait_until(self, locator: tuple, condition, timeout: int = timeout) -> WebElement:
        """Wait for a certain condition to be true for an element before proceeding."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(condition(locator))

    def wait_until_not(self, locator: tuple, condition, timeout: int = timeout) -> WebElement:
        """Waits until a specific condition is not met for an element."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until_not(condition(locator))

    def scroll_into_view(self, element: WebElement) -> WebElement:
        """Scroll the web page to make an element visible."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def _wait_for_element_and_scroll(self, locator: tuple) -> WebElement:
        """Waits for an element to be visible and scrolls it into view, then returns the WebElement."""
        element = self.wait_until(locator, ec.visibility_of_element_located)
        self.scroll_into_view(element)
        return element

    def click(self, locator: tuple):
        """Click on an element identified by a locator after ensuring it is clickable and in view."""
        element = self._wait_for_element_and_scroll(locator)
        element.click()

    def type(self, locator: tuple, text: str):
        """Sends keys to the element specified by locator after ensuring it is visible and in view."""
        element = self._wait_for_element_and_scroll(locator)
        element.clear()
        element.send_keys(text)

    def is_element_displayed(self, locator: tuple):
        """Checks if an element is displayed."""
        return self.wait_until(locator, ec.visibility_of_element_located)

    def is_element_not_displayed(self, locator: tuple):
        """Checks if an element is displayed."""
        return self.wait_until_not(locator, ec.visibility_of_element_located)

    def hover_over(self, locator: tuple):
        """Hover over an element identified by a locator after ensuring it is visible and in view."""
        element = self._wait_for_element_and_scroll(locator)
        self.action_chains.move_to_element(element).perform()

    def get_css_property(self, locator: tuple, css_property: str) -> str:
        """Get css property of an element."""
        element = self.wait_until(locator, ec.presence_of_element_located)
        return element.value_of_css_property(css_property)

    def get_element_by_attribute(self, locator: tuple, attribute_name: str):
        """Get an attribute value by an element."""
        element = self._wait_for_element_and_scroll(locator)
        return element.get_attribute(attribute_name)

    def check_elements_number(self, locator: tuple, expected_number: int):
        """Counts the elements matched by the specified locator and compares with expected number"""
        self.wait_until(locator, ec.presence_of_all_elements_located)
        elements = self.driver.find_elements(locator)
        actual_number = len(elements)
        return actual_number == expected_number

    def check_element_attribute(self, locator: tuple, attribute_name: str, expected_value: str):
        """Verifies that value of a specified attribute of a specified element matches the expected value."""
        element = self._wait_for_element_and_scroll(locator)
        actual_value = element.get_attribute(attribute_name)
        return actual_value == expected_value


