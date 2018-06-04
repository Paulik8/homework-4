from components.auth_form import AuthForm
from pages.page import Page


class AuthPage(Page):
    LOGOUT_URL = 'https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose'

    def __init__(self, driver):
        super(AuthPage, self).__init__(driver)
        self.auth_form = AuthForm(self.driver)

    def login(self, login, password):
        self.auth_form.get_login().send_keys(login)
        self.auth_form.get_password().send_keys(password)
        self.auth_form.submit().click()

    def logout(self):
        self.driver.get(self.LOGOUT_URL)

    # def add_profile(self):
    #     self.auth_form.get_add_profile_button().click()

    def clear_inputs(self):
        self.auth_form.get_login().clear()
        self.auth_form.get_password().clear()


    def re_login(self, login, password):
    	self.auth_form.get_add_profile_button().click()
    	self.login(login, password)