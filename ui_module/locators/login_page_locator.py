from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    """
    list of login page locators
    """

    EMAIL_FIELD = (By.ID, 'fld-e')
    PASSWORD_FIELD = (By.ID, 'fld-p1')
    LOGIN_BTN = (By.CLASS_NAME, 'c-button-secondary')
