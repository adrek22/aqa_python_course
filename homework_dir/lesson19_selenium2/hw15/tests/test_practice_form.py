import pytest

from homework_dir.lesson19_selenium2.hw15.pages.home_page import HomePage


def test_home_page(driver):
    """Verifies that the essential elements on the Home page are displayed."""
    home_page = HomePage(driver)
    assert home_page.home_btn_is_displayed, "Home button should be visible on the page."
    assert home_page.header_img_is_displayed, "Header image should be visible on the page."
    assert home_page.forms_btn_is_displayed, "Forms section button should be visible on the page."


def test_forms_page(driver):
    """Verifies the behavior and visibility of elements on the Forms page."""
    home_page = HomePage(driver)
    forms_page = home_page.click_on_forms_btn()

    # Verify visibility of elements
    assert forms_page.forms_top_text_is_displayed, "Top text should be visible on the Forms page."
    assert forms_page.forms_option_is_displayed, "Forms option should be visible in the left list."
    assert forms_page.practice_form_option_is_displayed, "Practice form option should be visible in the left list."

    assert forms_page.count_number_of_left_panel_items, "There should be 6 main items in left list."

    # Verify list collapsing/expanding
    forms_page.click_on_forms_in_list()
    assert forms_page.practice_form_option_is_not_displayed, "Practice form option should be not visible in the left list as list is collapsed."
    forms_page.click_on_forms_in_list()
    assert forms_page.practice_form_option_is_displayed, "Practice form option should be visible again in the left list."


def test_practice_form_page(driver):
    """
    Validates various functionalities and display elements on the Practice Form page.

    Steps:
    - Navigates to the Forms button and clicks it to go to the forms section.
    - Selects the Practice Form from the forms list to navigate to the practice form page.
    - Checks various elements on the practice form for visibility and correct text.
    - Fills out the form with test data and submits it.
    - Verifies that the summary dialog appears with the correct information.
    - Closes the dialog after submission to clean up the state.

    Asserts:
    - All specified page elements are visible.
    - Text labels and placeholders have expected content.
    - The form submits correctly and displays a summary with correct data.
    """

    # Navigate from home page to the forms page and then to the practice form
    home_page = HomePage(driver)
    forms_page = home_page.click_on_forms_btn()
    practice_form_page = forms_page.click_on_practice_form_in_list()

    # Check visibility of elements on the form page
    assert practice_form_page.header_text_is_displayed, "Header text should be visible on the Practice Form page."
    assert practice_form_page.form_title_is_displayed, "Form title should be visible."
    assert practice_form_page.name_label_is_displayed, "Name label should be visible."
    assert practice_form_page.gender_label_is_displayed, "Gender label should be visible."
    assert practice_form_page.mobile_label_is_displayed, "Mobile number label should be visible."
    assert practice_form_page.submit_btn_is_displayed, "Submit button should be visible."

    # Check the accuracy of text labels and placeholders
    assert practice_form_page.name_label_text_check, "Name label text does not match expected text."
    assert practice_form_page.gender_label_text_check, "Gender label text does not match expected text."
    assert practice_form_page.mobile_label_text_check, "Mobile number label text does not match expected text."
    assert practice_form_page.submit_btn_text_check, "Submit button text does not match expected text."

    # Check placeholders text
    assert practice_form_page.first_name_placeholder_check, "Placeholder's text of First Name field does not match expected text."
    assert practice_form_page.last_name_placeholder_check, "Placeholder's text of Last Name field does not match expected text."
    assert practice_form_page.mobile_number_placeholder_check, "Placeholder's text of Mobile Number field does not match expected text."

    # Fill the form and submit it
    practice_form_page.type_first_name('Mike')
    practice_form_page.type_last_name('Tyson')
    practice_form_page.select_gender_radio_btn(' mAle')
    practice_form_page.type_mobile_number('3105504000')
    practice_form_page.click_on_submit_btn()

    # Validate the summary dialog post submission
    assert practice_form_page.summary_dialog_is_displayed, "Summary label should be visible after the form submitting."
    assert practice_form_page.dialog_title_is_displayed, "Dialog title should be visible."
    assert practice_form_page.dialog_table_is_displayed, "Dialog table should be visible."
    assert practice_form_page.dialog_close_btn_is_displayed, "Close button in dialog should be visible."

    # Check values in the summary dialog
    assert practice_form_page.table_student_name_label_check, "Student Name table label does not match expected text."
    assert practice_form_page.table_gender_label_check, "Gender table label does not match expected text."
    assert practice_form_page.table_mobile_label_check, "Mobile table label does not match expected text."
    assert practice_form_page.table_student_name_value_get() == 'Mike Tyson', "Student Name table value does not match expected text."
    assert practice_form_page.table_gender_value_get() == 'Male', "Gender table value does not match expected text."
    assert practice_form_page.table_mobile_value_get() == '3105504000', "Mobile table value does not match expected text."

    # Close the dialog to end the test
    practice_form_page.click_on_dialog_close_btn()


@pytest.mark.xfail
# @pytest.mark.skip('Bug or wrong test')
def test_button_color_changing_after_hovering(driver):
    home_page = HomePage(driver)
    forms_page = home_page.click_on_forms_btn()
    practice_form_page = forms_page.click_on_practice_form_in_list()

    color_before_hover = practice_form_page.get_color_submit_btn
    practice_form_page.hover_over_submit_btn()
    color_after_hover = practice_form_page.get_color_submit_btn
    assert color_after_hover != color_before_hover, f"Submit button color should change on hover. Before: {color_before_hover}, After: {color_after_hover}"
