from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from AutomationHomeAssignment.ui_module.locators.country_locator import CountryLocator


class CountryPageElements:

    def __init__(self, driver, delay=11, long_delay=120):
        self.name = self.__class__.__name__
        self.driver = driver
        self.url = 'https://www.bestbuy.com/'
        self.wait = WebDriverWait(self.driver, delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])
        self.long_wait = WebDriverWait(self.driver, long_delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])

    def open_url(self):
        self.driver.get(self.url)

    def select_usa_site(self):
        element = self.wait.until(ec.element_to_be_clickable(CountryLocator.COUNTRY_USA))
        element.click()

    def select_canada__site(self):
        self.wait.until(ec.element_to_be_clickable(CountryLocator.COUNTRY_CANADA)).click()
