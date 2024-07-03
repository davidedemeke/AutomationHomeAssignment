from AutomationHomeAssignment.ui_module.page_elements.country_page_elements import CountryPageElements
from AutomationHomeAssignment.ui_module.page_elements.home_page_elements import HomePageElements
from AutomationHomeAssignment.ui_module.page_elements.login_page_elements import LoginPageElements


class CountryPage(CountryPageElements, HomePageElements, LoginPageElements):

    def open_browser(self):
        CountryPageElements.open_url(self)
        CountryPageElements.select_usa_site(self)

    def navigate_to_website_and_search_products(self):
        HomePageElements.click_on_my_account_tab(self)
        HomePageElements.click_on_sign_in_btn(self)
        LoginPageElements.find_and_insert_login_data(self)
        LoginPageElements.click_on_submit_btn(self)
        HomePageElements.insert_text_in_search_bar(self)
