from selenium.webdriver.common.by import By


def by(locator: str) -> tuple:
    """
    Determines the appropriate Selenium By type based on the provided locator string.

    Args:
        locator (str): The locator string used to find elements on a web page.

    Returns:
        tuple: A tuple containing the By type and the locator value.

    Raises:
        ValueError: If the locator type is not supported or is unrecognized.
    """
    if locator.startswith(("//", "(//")):
        return By.XPATH, locator
    elif locator.startswith('name='):
        return By.NAME, locator[5:]
    elif locator.startswith('id='):
        return By.ID, locator[3:]
    elif locator.startswith('class='):
        return By.CLASS_NAME, locator[6:]
    elif locator.startswith('contain_text='):
        return By.XPATH, f"//*[contains(text(), '{locator[13:]}')]"
    elif locator.startswith('link_text='):
        return By.LINK_TEXT, locator[10:]
    elif locator.startswith('css='):
        return By.CSS_SELECTOR, locator[4:]
    elif locator.startswith('tag='):
        return By.TAG_NAME, locator[4:]
    else:
        raise ValueError(f"Unsupported locator type provided: {locator}")

