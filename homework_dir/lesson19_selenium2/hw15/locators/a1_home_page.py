"""
This module contains the locators for Home page within the web application tested,
using different strategies provided by Selenium WebDriver. These locators are used by the page objects
to interact with the web elements during test execution.

The locators are defined using a utility function `by` which simplifies the creation
of locator tuples by interpreting string inputs to determine the appropriate Selenium By strategies.
"""
from homework_dir.lesson19_selenium2.hw15.utils.by import by
body_tag = by('tag=body')  # needed as locator to wait for page to load

home_url = by('//a[@href="https://1demoqa.com"]')
header_img = by('//img[@src="/images/1Toolsqa.jpg"]')
forms_section_btn = by('text=Forms')
