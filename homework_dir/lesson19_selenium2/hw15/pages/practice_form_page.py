from selenium.webdriver.remote.webdriver import WebDriver
from homework_dir.lesson19_selenium2.hw15.locators import a3_practice_form_page
from homework_dir.lesson19_selenium2.hw15.pages.base_page import BasePage


class PracticeFormPage(BasePage):
    """
    Represents the Practice Form page functionalities, providing methods to interact with the form's elements.
    """
    title = "Practice Form"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def header_text_is_displayed(self):
        """Checks if the header text is displayed on Practice Form page."""
        return self.is_element_displayed(a3_practice_form_page.practice_form_header_txt)

    def form_title_is_displayed(self):
        """Checks if the form title is displayed."""
        return self.is_element_displayed(a3_practice_form_page.form_title)

    def name_label_is_displayed(self):
        """Checks if the Name label is displayed."""
        return self.is_element_displayed(a3_practice_form_page.user_name_form_lbl)

    def gender_label_is_displayed(self):
        """Checks if the Gender label is displayed."""
        return self.is_element_displayed(a3_practice_form_page.gender_form_lbl)

    def mobile_label_is_displayed(self):
        """Checks if the Mobile label is displayed."""
        return self.is_element_displayed(a3_practice_form_page.mobile_number_form_lbl)

    def submit_btn_is_displayed(self):
        """Checks if the Submit button is displayed."""
        return self.is_element_displayed(a3_practice_form_page.submit_btn)

    def summary_dialog_is_displayed(self):
        """Checks if the Summary dialog is displayed after form submitting."""
        return self.is_element_displayed(a3_practice_form_page.summary_dialog_container)

    def dialog_title_is_displayed(self):
        """Checks if the dialog title  is displayed."""
        return self.is_element_displayed(a3_practice_form_page.dialog_title)

    def dialog_table_is_displayed(self):
        """Checks if the dialog table is displayed."""
        return self.is_element_displayed(a3_practice_form_page.dialog_table)

    def dialog_close_btn_is_displayed(self):
        """Checks if the dialog Close button is displayed."""
        return self.is_element_displayed(a3_practice_form_page.dialog_close_btn)

    def name_label_text_check(self, attribute_name='text', text='Name'):
        """Checks the text of Name label."""
        return self.check_element_attribute(a3_practice_form_page.user_name_form_lbl, attribute_name, text)

    def gender_label_text_check(self, attribute_name='text', text='Gender'):
        """Checks if the Gender label is displayed."""
        return self.check_element_attribute(a3_practice_form_page.gender_form_lbl, attribute_name, text)

    def mobile_label_text_check(self, attribute_name='text', text='Mobile'):
        """Checks if the Mobile label is displayed."""
        return self.check_element_attribute(a3_practice_form_page.mobile_number_form_lbl, attribute_name, text)

    def submit_btn_text_check(self, attribute_name='text', text: str = "Submit"):
        """Checks if the Mobile label is displayed."""
        return self.check_element_attribute(a3_practice_form_page.submit_btn, attribute_name, text)

    def hover_over_submit_btn(self):
        """Performs a mouse hover action over the 'Submit' button."""
        self.hover_over(a3_practice_form_page.submit_btn)

    def get_color_submit_btn(self, attribute_name='background-color'):
        """Get background color of the Submit button."""
        return self.get_css_property(a3_practice_form_page.submit_btn, attribute_name)

    def first_name_placeholder_check(self, attribute_name='placeholder', expected_value='First Name'):
        """Get placeholder value of the First Name field."""
        return self.check_element_attribute(a3_practice_form_page.first_name_inp, attribute_name, expected_value)

    def last_name_placeholder_check(self, attribute_name='placeholder', expected_value='Last Name'):
        """Get placeholder value of the First Name field."""
        return self.check_element_attribute(a3_practice_form_page.last_name_inp, attribute_name, expected_value)

    def mobile_number_placeholder_check(self, attribute_name='placeholder', expected_value='Mobile Number'):
        """Get placeholder value of the First Name field."""
        return self.check_element_attribute(a3_practice_form_page.mobile_number_inp, attribute_name, expected_value)

    def type_first_name(self, text):
        """Enters text into the 'First Name' input field."""
        self.type(a3_practice_form_page.first_name_inp, text)

    def type_last_name(self, text):
        """Enters text into the 'Last Name' input field."""
        self.type(a3_practice_form_page.last_name_inp, text)

    def select_gender_radio_btn(self, gender='male'):
        """Selects a gender radio button based on the provided gender."""
        gender_map = {
            'male': 1,
            'female': 2,
            'other': 3
        }
        gender_index = gender_map.get(gender.lower().strip(), 1)
        locator = a3_practice_form_page.gender_radio_lbl(gender_index)
        self.click(locator)

    def type_mobile_number(self, text):
        """Enters a mobile number into the 'Mobile Number' input field."""
        self.type(a3_practice_form_page.mobile_number_inp, text)

    def click_on_submit_btn(self):
        """Clicks the 'Submit' button on the form."""
        self.click(a3_practice_form_page.submit_btn)

    def table_student_name_label_check(self, attribute_name='text', text='Student Name'):
        """Checks the text of Student Name label."""
        return self.check_element_attribute(a3_practice_form_page.table_1st_row_label, attribute_name, text)

    def table_student_name_value_get(self, attribute_name='textContent'):
        """Checks the value of Student Name label."""
        return self.get_element_by_attribute(a3_practice_form_page.table_1st_row_value, attribute_name)

    def table_gender_label_check(self, attribute_name='text', text='Gender'):
        """Checks the text of Gender label."""
        return self.check_element_attribute(a3_practice_form_page.table_3rd_row_label, attribute_name, text)

    def table_gender_value_get(self, attribute_name='textContent'):
        """Checks the value of Gender label."""
        return self.get_element_by_attribute(a3_practice_form_page.table_3rd_row_value, attribute_name)

    def table_mobile_label_check(self, attribute_name='text', text='Mobile'):
        """Checks the text of Mobile label."""
        return self.check_element_attribute(a3_practice_form_page.table_4th_row_label, attribute_name, text)

    def table_mobile_value_get(self, attribute_name='textContent'):
        """Checks the value of Mobile label."""
        return self.get_element_by_attribute(a3_practice_form_page.table_4th_row_value, attribute_name)

    def click_on_dialog_close_btn(self):
        """Clicks the close button on the dialog that appears after form submission."""
        self.click(a3_practice_form_page.dialog_close_btn)


class PracticeFormPageHandler(PracticeFormPage):
    """
    Handlers use predefined methods from Page. Methods indicate verbs. e.g. login(), type_password(), send_feedback()
    """
    def assert_practice_form(self):
        """
        Performs a comprehensive check of visible elements, label texts,
        and placeholder texts on the Practice Form page.
        """
        color_before_hover = self.get_color_submit_btn()
        self.hover_over_submit_btn()
        color_after_hover = self.get_color_submit_btn()
        field_checks1 = {
            f'Submit button color is changed from {color_before_hover} to {color_after_hover}': (
                color_after_hover != color_before_hover,
                f"Submit button color should change on hover. Before: {color_before_hover}, After: {color_after_hover}")
        }
        field_checks2 = {
            'Header text is visible': (self.header_text_is_displayed, "Header text should be visible on the Practice Form page."),
            'Form title is visible': (self.form_title_is_displayed, "Form title should be visible."),
            'Name label is visible': (self.name_label_is_displayed, "Name label should be visible."),
            'Gender label is visible': (self.gender_label_is_displayed, "Gender label should be visible."),
            'Mobile number label is visible': (self.mobile_label_is_displayed, "Mobile number label should be visible."),
            'Submit button is visible': (self.submit_btn_is_displayed, "Submit button should be visible."),
            'Name label text matches expected': (self.name_label_text_check, "Name label text does not match expected text."),
            'Gender label text matches expected': (self.gender_label_text_check, "Gender label text does not match expected text."),
            'Mobile number label text matches expected': (self.mobile_label_text_check, "Mobile number label text does not match expected text."),
            'Submit button text matches expected': (self.submit_btn_text_check, "Submit button text does not match expected text."),
            'First Name placeholder text matches expected': (self.first_name_placeholder_check, "Placeholder's text of First Name field does not match expected text."),
            'Last Name placeholder text matches expected': (self.last_name_placeholder_check, "Placeholder's text of Last Name field does not match expected text."),
            'Mobile Number placeholder text matches expected': (self.mobile_number_placeholder_check, "Placeholder's text of Mobile Number field does not match expected text.")
        }
        self.soft_assert(field_checks1)
        self.soft_assert(field_checks2)

    def fill_out_form_and_submit(self, first_name, last_name, gender, mobile):
        """Fill the form and submit it"""
        self.type_first_name(first_name)
        self.type_last_name(last_name)
        self.select_gender_radio_btn(gender)
        self.type_mobile_number(mobile)
        self.click_on_submit_btn()

    def assert_summary_dialog(self, student_name, gender, mobile):
        """Validate the summary dialog post submission and check values in the summary dialog"""
        field_checks = {
            'Header text is visible': (self.summary_dialog_is_displayed, "Summary label should be visible after the form submitting."),
            'Form title is visible': (self.dialog_title_is_displayed, "Dialog title should be visible."),
            'Name label is visible': (self.dialog_table_is_displayed, "Dialog table should be visible."),
            'Gender label is visible': (self.dialog_close_btn_is_displayed, "Close button in dialog should be visible."),
            'Mobile number label is visible': (self.table_student_name_label_check, "Student Name table label does not match expected text."),
            'Submit button is visible': (self.table_gender_label_check, "Gender table label does not match expected text."),
            'Name label text matches expected': (self.table_mobile_label_check, "Mobile table label does not match expected text."),
            f'Gender label text matches expected: {student_name}': (
                self.table_student_name_value_get() == student_name,
                f"Student Name table value does not match. "
                f"Expected: {student_name}, Found: {self.table_student_name_value_get()}"),
            f'Mobile number label text matches expected: {gender}': (
                self.table_gender_value_get() == gender,
                f"Gender table value does not match. "
                f"Expected: {gender}, Found: {self.table_gender_value_get()}"),
            f'Submit button text matches expected: {mobile}':
                (self.table_mobile_value_get() == mobile,
                 f"Mobile table value does not match. "
                 f"Expected: {mobile}, Found: {self.table_mobile_value_get()}")
        }
        print("\nSummary dialog is opened")
        self.soft_assert(field_checks)

    def close_summary_dialog(self):
        self.click_on_dialog_close_btn()






