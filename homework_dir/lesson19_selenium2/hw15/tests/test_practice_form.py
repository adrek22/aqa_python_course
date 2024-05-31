import os
import allure
import pytest

from homework_dir.lesson19_selenium2.hw15.pages.home_page import HomePageHandler, HomePage
from homework_dir.lesson19_selenium2.hw15.pages.forms_page import FormsPageHandler, FormsPage
from homework_dir.lesson19_selenium2.hw15.pages.practice_form_page import PracticeFormPageHandler, PracticeFormPage
from homework_dir.lesson19_selenium2.hw15.tests.test_data.test_data import select_random_data


@allure.title("Flow testing")
@allure.description("Verifies the flow from Home page to Practice Form page.")
@allure.tag("Home page", "Forms  page", "Practice Form page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("UI Tests")
@allure.suite("Demo website")
@allure.sub_suite("Practice Form page")
@allure.feature("Practice Form page testing")
def test_flow(driver):
    """Verifies the flow."""
    with HomePageHandler(driver) as handler1:
        """Verifies that the essential elements on the Home page are displayed."""
        handler1.assert_home_page()
        handler1.open_forms_page()

    with FormsPageHandler(driver) as handler2:
        """Verifies the behavior and visibility of elements on the Forms page."""
        handler2.assert_forms_page()
        handler2.open_practice_form()

    with PracticeFormPageHandler(driver) as handler3:
        """Validates various functionalities and display elements on the Practice Form page."""
        handler3.assert_practice_form()
        file_path = os.path.join(os.path.dirname(__file__), 'test_data', 'test_data.csv')
        random_row = select_random_data(file_path)
        first_name = random_row['First Name']
        last_name = random_row['Last Name']
        gender = random_row['Gender']
        mobile_number = random_row['Mobile Number']
        handler3.fill_out_form_and_submit(first_name=first_name, last_name=last_name, gender=gender, mobile=mobile_number)
        handler3.assert_summary_dialog(student_name=first_name+'123 '+last_name, gender=gender.capitalize(), mobile=mobile_number)
        # handler3.screenshot()
        handler3.close_summary_dialog()


# @pytest.mark.xfail
@pytest.mark.skip('Not Actual')
def test_button_color_changing_after_hovering(driver):
    home_page, forms_page, practice_form_page = HomePage(driver), FormsPage(driver), PracticeFormPage(driver)
    home_page.click_on_forms_btn()
    forms_page.click_on_practice_form_in_list()
