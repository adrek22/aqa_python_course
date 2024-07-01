from homework_dir.lesson19_selenium2.hw15.driver import shared_driver
from homework_dir.lesson19_selenium2.hw15.locators import a1_home_page
from homework_dir.lesson19_selenium2.hw15.pages.base_page import BasePage
from homework_dir.lesson19_selenium2.hw15.utils.soft_step import step


class HomePage(BasePage):
    """
    Represents the homepage of the website with methods that encapsulate the
    functionalities available on this page.
    """
    title = "Home"

    def __init__(self, driver: shared_driver.driver):
        super().__init__(driver)

    def home_url_is_displayed(self):
        """Checks if the home url is displayed."""
        return self.is_element_displayed(a1_home_page.home_url)

    def home_btn_is_displayed(self):
        """Checks if the home button is displayed."""
        return self.is_element_displayed(a1_home_page.header_img)

    def forms_btn_is_displayed(self):
        """Checks if the forms section button is displayed."""
        return self.is_element_displayed(a1_home_page.forms_section_btn)

    def click_on_forms_btn(self):
        """Is used to navigate from the homepage to the Forms section of the site."""
        self.click(a1_home_page.forms_section_btn)


class HomePageHandler(HomePage):
    """
    Handlers use predefined methods from Page. Methods indicate verbs. e.g. login(), type_password(), send_feedback()
    """
    def assert_home_page(self):
        field_checks = {
            'Home url element is visible': (
                self.home_url_is_displayed(), "Home url element should be visible on the page."),
            'Home button by image is visible': (
                self.home_btn_is_displayed(), "Home button should be visible on the page."),
            'Forms section button is visible': (
                self.forms_btn_is_displayed(), "Forms section button should be visible on the page.")
        }

        return self.soft_assert(field_checks)

    def open_forms_page(self):
        self.click_on_forms_btn()
