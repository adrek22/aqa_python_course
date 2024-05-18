from selenium.webdriver.remote.webdriver import WebDriver
from homework_dir.lesson19_selenium2.hw15.locators import a2_forms_page
from homework_dir.lesson19_selenium2.hw15.pages.base_page import BasePage


class FormsPage(BasePage):
    """
    FormsPage provides methods to navigate and interact with the forms section
    of the DemoQA website.
    """
    title = "Forms"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def forms_top_text_is_displayed(self):
        """Checks if the top text is displayed on Forms page."""
        return self.is_element_displayed(a2_forms_page.forms_top_txt)

    def forms_option_is_displayed(self):
        """Checks if the Forms option is displayed in left list."""
        return self.is_element_displayed(a2_forms_page.forms_list_option)

    def practice_form_option_is_displayed(self):
        """Checks if the Practice form option button is displayed in left list."""
        return self.is_element_displayed(a2_forms_page.practice_form_list_option)

    def practice_form_option_is_not_displayed(self):
        """Checks if the Practice form option button is not displayed in left list."""
        return self.is_element_not_displayed(a2_forms_page.practice_form_list_option)

    def count_number_of_left_panel_items(self):
        """Checks the number of items in left list."""
        return self.check_elements_number(a2_forms_page.left_panel_item, 6)

    def click_on_forms_in_list(self):
        """Clicks on the 'Forms' list option to expand/collapse the 'Forms' list section."""
        self.click(a2_forms_page.forms_list_option)

    def click_on_practice_form_in_list(self):
        """Clicks on the 'Practice Form' list option to navigate to the Practice Form page."""
        self.click(a2_forms_page.practice_form_list_option)


class FormsPageHandler(FormsPage):
    """
    Handlers use predefined methods from Page. Methods indicate verbs. e.g. login(), type_password(), send_feedback()
    """
    def assert_forms_page(self):
        # Verify visibility of elements
        field_checks1 = {
            'Top text is visible': (self.forms_top_text_is_displayed, "Top text should be visible on the Forms page."),
            'Forms option is visible': (self.forms_option_is_displayed, "Forms option should be visible in the left list."),
            'Practice form option button is visible': (self.practice_form_option_is_displayed, "Practice form option should be visible in the left list."),
            'There are 6 main items in left list.': (self.count_number_of_left_panel_items, "There should be 6 main items in left list.")
        }
        field_checks2 = {
            'Practice form option is not visible': (self.practice_form_option_is_not_displayed, "Practice form option should be not visible in the left list as list is collapsed."),
        }
        field_checks3 = {
            'Practice form option is visible': (self.practice_form_option_is_displayed, "Practice form option should be visible again in the left list."),
        }
        self.soft_assert(field_checks1)

        # Verify list collapsing/expanding
        self.click_on_forms_in_list()
        self.soft_assert(field_checks2)
        self.click_on_forms_in_list()
        self.soft_assert(field_checks3)

    def open_practice_form(self):
        self.click_on_practice_form_in_list()
