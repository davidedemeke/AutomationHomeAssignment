import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from AutomationHomeAssignment.ui_module.page_elements.home_page_elements import HomePageElements


def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
class TestScenariosClass:

    def test_login_to_my_account(self, driver):
        """Test login to account and assert url is correct"""
        driver.CountryPage(driver)
        driver.open_browser()
        assert driver.url == driver.current_url, f'Url of the opened website is not match, expected: {driver.url} , got {driver.current_url}'

    def test_skip_phone_number_popup(self, driver):
        """Test search item and validate results are identity to the searched item  AND verify pop up is skipped if needed"""
        home_page = HomePageElements(driver)
        home_page.insert_text_in_search_bar()
        home_page.click_skip_phone_number_popup()
        assert home_page.is_skip_phone_number_popup_closed(), "Phone number popup is not closed"
