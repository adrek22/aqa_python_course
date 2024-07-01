import logging
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
    home_page, forms_page, practice_form_page = HomePageHandler(driver), FormsPageHandler(driver), PracticeFormPageHandler(driver)
    """Verifies that the essential elements on the Home page are displayed."""
    logging.info(f"Page loaded: {home_page.title}")
    errors = home_page.assert_home_page()
    home_page.open_forms_page()

    """Verifies the behavior and visibility of elements on the Forms page."""
    logging.info(f"Page loaded: {forms_page.title}")
    errors += forms_page.assert_forms_page()
    forms_page.open_practice_form()

    """Validates various functionalities and display elements on the Practice Form page."""
    logging.info(f"Page loaded: {practice_form_page.title}")
    errors += practice_form_page.assert_practice_form()
    file_path = os.path.join(os.path.dirname(__file__), 'test_data', 'test_data.csv')
    random_row = select_random_data(file_path)
    first_name = random_row['First Name']
    last_name = random_row['Last Name']
    gender = random_row['Gender']
    mobile_number = random_row['Mobile Number']
    practice_form_page.fill_out_form_and_submit(first_name=first_name, last_name=last_name, gender=gender,
                                                mobile=mobile_number)
    errors += practice_form_page.assert_summary_dialog(student_name=first_name + ' ' + last_name,
                                                       gender=gender.capitalize(), mobile=mobile_number)
    practice_form_page.close_summary_dialog()

    if errors:
        error_messages = "\n".join(errors)
        raise AssertionError(f"Encountered errors in form validation:\n{error_messages}")


@allure.title('Assert that Home page elements are displayed and open Forms page')
def test_home_page(driver):
    home_page = HomePage(driver)
    assert home_page.home_url_is_displayed(), "Home url element should be visible on the page.."
    assert home_page.home_btn_is_displayed(), "Home button should be visible on the page."
    assert home_page.forms_btn_is_displayed(), "Forms section button should be visible on the page."
    home_page.click_on_forms_btn()


# @pytest.mark.xfail
@pytest.mark.skip('Not Actual')
def test_button_color_changing_after_hovering(driver):
    home_page, forms_page, practice_form_page = HomePage(driver), FormsPage(driver), PracticeFormPage(driver)
    home_page.click_on_forms_btn()
    forms_page.click_on_practice_form_in_list()
