from selenium.webdriver.common.by import By


class HomePageLocator(object):
    """
    list of home page locators
    """

    ACCOUNT = (By.CLASS_NAME, 'v-p-right-xxs line-clamp')
    SIGN_IN_BTN = (By.CLASS_NAME, 'c-button c-button-secondary c-button-sm sign-in-btn')
    CREATE_ACCOUNT_BTN = (By.CLASS_NAME, 'c-button c-button-outline c-button-sm create-account-btn')
    SEARCH_FIELD = (By.ID, 'gh-search-input')
    SKIP_POPUP = (By.ID, 'gh-search-input')
    SKIP_PHONE_NUMBER_POPUP = (By.ID, 'gh-search-input')
