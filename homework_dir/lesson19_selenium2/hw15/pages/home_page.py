from selenium.webdriver.remote.webdriver import WebDriver
from homework_dir.lesson19_selenium2.hw15.locators import locators
from homework_dir.lesson19_selenium2.hw15.pages.base_page import BasePage


class HomePage(BasePage):
    """
    Represents the homepage of the website with methods that encapsulate the
    functionalities available on this page.
    """
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def home_btn_is_displayed(self):
        """Checks if the home button is displayed."""
        return self.is_element_displayed(locators.home_btn)

    def header_img_is_displayed(self):
        """Checks if the header image is displayed."""
        return self.is_element_displayed(locators.header_img)

    def forms_btn_is_displayed(self):
        """Checks if the forms section button is displayed."""
        return self.is_element_displayed(locators.forms_section_btn)

    def click_on_forms_btn(self):
        """Is used to navigate from the homepage to the Forms section of the site."""
        self.click(locators.forms_section_btn)
