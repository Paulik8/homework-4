from components.page import Page
from components.base_settings_component import BaseSettingsForm

class BaseSettingsPage(Page):
    def personal_data(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        return baseSettingsForm.personal_data()
    def profile_get(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        return baseSettingsForm.profile_get()
    def profile(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        baseSettingsForm.profile_click()


