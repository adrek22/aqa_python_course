import os
import configparser
import platform
import subprocess
import datetime
import logging


from homework_dir.lesson19_selenium2.hw15 import config


def get_driver_version(browser_name: str) -> str:
    """Retrieves the version of the browser driver."""
    if browser_name == 'chrome':
        output = subprocess.check_output(['chromedriver', '--version']).decode().strip()
        version = output.split()[1]
    elif browser_name == 'firefox':
        output = subprocess.check_output(['geckodriver', '--version']).decode().strip()
        version = output.split()[1]
    else:
        version = 'Unknown'
    return version


def parse_requirements(file_path="../../../../requirements.txt") -> dict:
    """Parses the requirements.txt file to extract tool versions."""
    tool_versions = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '==' in line:
                tool, version = line.strip().split('==')
                tool_versions[tool.lower()] = version
    return tool_versions


def generate_environment_properties(browser_version):
    """
    Generates the environment properties and saves them to a file.

    Args:
        config (configparser.ConfigParser): The configuration parser object.
        browser_version (str): The version of the browser being used.

    Returns:
        None
    """
    tool_versions = parse_requirements()
    properties = {
        "Browser": config.browser.type,
        "Browser.Version": browser_version,
        "Browser.Driver.Version": get_driver_version(config.browser.type),
        "Browser.Wait.Timeout": config.browser.timeout,
        "Supported.Browsers": config.browser.supported_browsers,
        "OS": platform.system(),
        "OS.Version": platform.version(),
        "Application.Version": config.browser.app_version,
        "Base.URL": config.browser.base_url,
        "Database.Type": config.browser.db_type,
        "Region": config.browser.region,  # DEV, QA, CT, LT, PR
        "Test.Runner": "pytest",
        "Test.Runner.Version": tool_versions.get('pytest', 'Unknown'),
        "Selenium.Version": tool_versions.get('selenium', 'Unknown'),
        "Allure.Version": tool_versions.get('allure-pytest', 'Unknown'),
        "Execution.Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Executor": "local machine"  # Jenkins, local machine
    }

    directory = os.path.join(os.getcwd(), 'allure-results')
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = "environment.properties"
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")
    logging.info(f"Environment data saved to {file_path}")
