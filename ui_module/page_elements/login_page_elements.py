import json
from AutomationHomeAssignment.ui_module.locators.login_page_locator import LoginPageLocator
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait


class LoginPageElements:

    def __init__(self, driver, delay=30, long_delay=120):
        self.name = self.__class__.__name__
        self.driver = driver
        self.wait = WebDriverWait(self.driver, delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])
        self.long_wait = WebDriverWait(self.driver, long_delay, ignored_exceptions=[StaleElementReferenceException, WebDriverException])

    def get_user_data(self):
        with open('../utiles/config.json', "r") as data:
            list_of_pets = json.load(data)
        return list_of_pets

    def find_and_insert_login_data(self):
        self.wait.until(ec.element_to_be_clickable(LoginPageLocator.EMAIL_FIELD)).send_keys(self.get_user_data()[0])
        self.wait.until(ec.element_to_be_clickable(LoginPageLocator.PASSWORD_FIELD)).send_keys(self.get_user_data()[1])

    def click_on_submit_btn(self):
        self.wait.until(ec.element_to_be_clickable(LoginPageLocator.LOGIN_BTN)).click()
