from AutomationHomeAssignment.ui_module.page_elements.home_page_elements import HomePageElements


class HomePage(HomePageElements):

    def click_on_login_page(self):
        HomePageElements.click_on_sign_in_btn(self)
        HomePageElements.click_on_sign_in_btn(self)
