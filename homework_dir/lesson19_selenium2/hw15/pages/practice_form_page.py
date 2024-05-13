from selenium.webdriver.remote.webdriver import WebDriver
from homework_dir.lesson19_selenium2.hw15.locators import locators
from homework_dir.lesson19_selenium2.hw15.pages.base_page import BasePage


class PracticeFormPage(BasePage):
    """
    Represents the Practice Form page functionalities, providing methods to interact with the form's elements.
    """
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def header_text_is_displayed(self):
        """Checks if the header text is displayed on Practice Form page."""
        return self.is_element_displayed(locators.practice_form_header_txt)

    def form_title_is_displayed(self):
        """Checks if the form title is displayed."""
        return self.is_element_displayed(locators.form_title)

    def name_label_is_displayed(self):
        """Checks if the Name label is displayed."""
        return self.is_element_displayed(locators.user_name_form_lbl)

    def gender_label_is_displayed(self):
        """Checks if the Gender label is displayed."""
        return self.is_element_displayed(locators.gender_form_lbl)

    def mobile_label_is_displayed(self):
        """Checks if the Mobile label is displayed."""
        return self.is_element_displayed(locators.mobile_number_form_lbl)

    def submit_btn_is_displayed(self):
        """Checks if the Submit button is displayed."""
        return self.is_element_displayed(locators.submit_btn)

    def summary_dialog_is_displayed(self):
        """Checks if the Summary dialog is displayed after form submitting."""
        return self.is_element_displayed(locators.summary_dialog_container)

    def dialog_title_is_displayed(self):
        """Checks if the dialog title  is displayed."""
        return self.is_element_displayed(locators.dialog_title)

    def dialog_table_is_displayed(self):
        """Checks if the dialog table is displayed."""
        return self.is_element_displayed(locators.dialog_table)

    def dialog_close_btn_is_displayed(self):
        """Checks if the dialog Close button is displayed."""
        return self.is_element_displayed(locators.dialog_close_btn)

    def name_label_text_check(self, attribute_name='text', text='Name'):
        """Checks the text of Name label."""
        return self.check_element_attribute(locators.user_name_form_lbl, attribute_name, text)

    def gender_label_text_check(self, attribute_name='text', text='Gender'):
        """Checks if the Gender label is displayed."""
        return self.check_element_attribute(locators.gender_form_lbl, attribute_name, text)

    def mobile_label_text_check(self, attribute_name='text', text='Mobile'):
        """Checks if the Mobile label is displayed."""
        return self.check_element_attribute(locators.mobile_number_form_lbl, attribute_name, text)

    def submit_btn_text_check(self, attribute_name='text', text: str = "Submit"):
        """Checks if the Mobile label is displayed."""
        return self.check_element_attribute(locators.submit_btn, attribute_name, text)

    def hover_over_submit_btn(self):
        """Performs a mouse hover action over the 'Submit' button."""
        self.hover_over(locators.submit_btn)

    def get_color_submit_btn(self, attribute_name='background-color'):
        """Get background color of the Submit button."""
        return self.get_css_property(locators.submit_btn, attribute_name)

    def first_name_placeholder_check(self, attribute_name='placeholder', expected_value='First Name'):
        """Get placeholder value of the First Name field."""
        return self.check_element_attribute(locators.first_name_inp, attribute_name, expected_value)

    def last_name_placeholder_check(self, attribute_name='placeholder', expected_value='Last Name'):
        """Get placeholder value of the First Name field."""
        return self.check_element_attribute(locators.last_name_inp, attribute_name, expected_value)

    def mobile_number_placeholder_check(self, attribute_name='placeholder', expected_value='Mobile Number'):
        """Get placeholder value of the First Name field."""
        return self.check_element_attribute(locators.mobile_number_inp, attribute_name, expected_value)

    def type_first_name(self, text):
        """Enters text into the 'First Name' input field."""
        self.type(locators.first_name_inp, text)

    def type_last_name(self, text):
        """Enters text into the 'Last Name' input field."""
        self.type(locators.last_name_inp, text)

    def select_gender_radio_btn(self, gender='male'):
        """Selects a gender radio button based on the provided gender."""
        if gender.lower().strip() == 'male':
            locator = locators.male_gender_radio_lbl
        elif gender.lower().strip() == 'female':
            locator = locators.female_gender_radio_lbl
        else:
            locator = locators.other_gender_radio_lbl
        self.click(locator)

    def type_mobile_number(self, text):
        """Enters a mobile number into the 'Mobile Number' input field."""
        self.type(locators.mobile_number_inp, text)

    def click_on_submit_btn(self):
        """Clicks the 'Submit' button on the form."""
        self.click(locators.submit_btn)

    def table_student_name_label_check(self, attribute_name='text', text='Student Name'):
        """Checks the text of Student Name label."""
        return self.check_element_attribute(locators.table_1st_row_label, attribute_name, text)

    def table_student_name_value_get(self, attribute_name='textContent'):
        """Checks the value of Student Name label."""
        return self.get_element_by_attribute(locators.table_1st_row_value, attribute_name)

    def table_gender_label_check(self, attribute_name='text', text='Gender'):
        """Checks the text of Gender label."""
        return self.check_element_attribute(locators.table_3rd_row_label, attribute_name, text)

    def table_gender_value_get(self, attribute_name='textContent'):
        """Checks the value of Gender label."""
        return self.get_element_by_attribute(locators.table_3rd_row_value, attribute_name)

    def table_mobile_label_check(self, attribute_name='text', text='Mobile'):
        """Checks the text of Mobile label."""
        return self.check_element_attribute(locators.table_4th_row_label, attribute_name, text)

    def table_mobile_value_get(self, attribute_name='textContent'):
        """Checks the value of Mobile label."""
        return self.get_element_by_attribute(locators.table_4th_row_value, attribute_name)

    def click_on_dialog_close_btn(self):
        """Clicks the close button on the dialog that appears after form submission."""
        self.click(locators.dialog_close_btn)