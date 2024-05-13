"""
This module contains the locators for Practice Form Page within the web application tested,
using different strategies provided by Selenium WebDriver. These locators are used by the page objects
to interact with the web elements during test execution.

The locators are defined using a utility function `by` which simplifies the creation
of locator tuples by interpreting string inputs to determine the appropriate Selenium By strategies.
"""
from homework_dir.lesson19_selenium2.hw15.utils.by import by

practice_form_header_txt = by('//h1[@class="text-center"]')
form_title = by('contain_text=Student Registration Form')
user_name_form_lbl = by('id=userName-label')
first_name_inp = by('id=firstName')
last_name_inp = by('id=lastName')
gender_form_lbl = by('//div[@id="genterWrapper"]/div[1]')
# male_gender_radio_lbl = by('//label[@for="gender-radio-1"]')
# female_gender_radio_lbl = by('//label[@for="gender-radio-2"]')
# other_gender_radio_lbl = by('//label[@for="gender-radio-3"]')
gender_radio_lbl = lambda index: by(f'//label[@for="gender-radio-{index}"]')
mobile_number_form_lbl = by('id=userNumber-label')
mobile_number_inp = by('id=userNumber')
submit_btn = by('id=submit')
summary_dialog_container = by('//div[@role="dialog"]')
dialog_title = by('id=example-modal-sizes-title-lg')
dialog_table = by('class=table table-dark table-striped table-bordered table-hover')
table_1st_row_label = by('//tbody/tr[1]/td[1]')
table_1st_row_value = by('//tbody/tr[1]/td[2]')
table_3rd_row_label = by('//tbody/tr[3]/td[1]')
table_3rd_row_value = by('//tbody/tr[3]/td[2]')
table_4th_row_label = by('//tbody/tr[4]/td[1]')
table_4th_row_value = by('//tbody/tr[4]/td[2]')
dialog_close_btn = by('id=closeLargeModal')