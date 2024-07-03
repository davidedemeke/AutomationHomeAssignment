from AutomationHomeAssignment.ui_module.locators.home_page_locator import HomePageLocator
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait


class HomePageElements:
    def __init__(self, driver, delay=30, long_delay=120):
        self.name = self.__class__.__name__
        self.driver = driver
        self.wait = WebDriverWait(self.driver, delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])
        self.long_wait = WebDriverWait(self.driver, long_delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])

    def click_on_my_account_tab(self):
        self.wait.until(ec.element_to_be_clickable(HomePageLocator.ACCOUNT)).click()

    def click_on_sign_in_btn(self):
        self.wait.until(ec.element_to_be_clickable(HomePageLocator.SIGN_IN_BTN)).click()

    def insert_text_in_search_bar(self):
        list_of_products = self.wait.until(ec.element_to_be_clickable(HomePageLocator.SEARCH_FIELD)).send_keys('hello').click()
        return list_of_products

    def click_skip_phone_number_popup(self):
        self.wait.until(ec.element_to_be_clickable(HomePageLocator.SKIP_POPUP)).click()

    def is_skip_phone_number_popup_closed(self):
        skip_button=self.wait.until(ec.element_to_be_clickable(HomePageLocator.SKIP_PHONE_NUMBER_POPUP))
        return not skip_button.is_displayed()
