from selenium import webdriver
from homework_dir.lesson19_selenium2.hw15 import config


def driver_factory(browser_name: str) -> webdriver:
    """
    Creates and returns a WebDriver instance based on the browser name provided.

    Raises:
        ValueError: If the specified browser is not supported or recognized.
    """
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        service = webdriver.FirefoxService(executable_path=r'C:\WebDriver\bin\geckodriver.exe')
        return webdriver.Firefox(options=options, service=service)
    else:
        try:
            browser_class = getattr(webdriver, browser_name.capitalize())
            return browser_class()
        except AttributeError:
            raise ValueError(f"Unsupported browser specified. Supported browsers: {config.browser.supported_browsers}")
