from selenium.webdriver.common.by import By


class CountryLocator(object):
    """
    list of select country page locators
    """

    COUNTRY_USA = (By.XPATH, '//a[@class="us-link"]/h4')
    COUNTRY_CANADA = (By.XPATH, '//a[contains(@class, "canada-link")]')
