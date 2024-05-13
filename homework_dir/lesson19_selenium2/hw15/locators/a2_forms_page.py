"""
This module contains the locators for Forms page within the web application tested,
using different strategies provided by Selenium WebDriver. These locators are used by the page objects
to interact with the web elements during test execution.

The locators are defined using a utility function `by` which simplifies the creation
of locator tuples by interpreting string inputs to determine the appropriate Selenium By strategies.
"""
from homework_dir.lesson19_selenium2.hw15.utils.by import by

left_panel_item = by('class=element-group')
forms_list_option = by('//div[@class="header-text" and text()="Forms"]')
forms_top_txt = by('contain_text=Please select an item from left to start practice.')
expanded_element_list = by('class=element-list collapse show')
practice_form_list_option = by('//span[@class="text" and text()="Practice Form"]')