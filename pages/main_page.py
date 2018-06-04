from components.group_component import GroupComponent
from components.main_up_toolbar import MainUpToolbar
from components.main_vertical_list import MainVerticalList
from pages.page import Page
from components.notification_component import NotificationComponent
from constants import game
import urlparse

from components.main_components import MainForm



class MainPage(Page):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.main_up_toolbar = MainUpToolbar(self.driver)
        self.main_vertical_list = MainVerticalList(self.driver)
        self.group_component = GroupComponent(self.driver)

    def open_friends_list(self):
        self.main_vertical_list.get_friends().click()

    def accept_notification(self):
        notification = NotificationComponent(self.driver)
        notification.accept_reletionship().click()

    def open_friends_list(self):
        self.main_vertical_list.get_friends().click()

    def my_name_surname(self):
        main_form = MainForm(self.driver)
        return main_form.get_name_surname()

    def my_birthday(self):
        main_form = MainForm(self.driver)
        return main_form.get_birthday()

    def my_birth_note(self):
        main_form = MainForm(self.driver)
        return main_form.get_birth_note()

    def my_current_city(self):
        main_form = MainForm(self.driver)
        return main_form.get_current_city()

    def open_games_list(self):
        self.main_vertical_list.get_games().click()

    def open_notes_list(self):
        self.main_vertical_list.get_more().click()
        self.main_vertical_list.get_notes().click()

    def open_notification(self):
        self.main_up_toolbar.get_notification().click()
        # self.main_up_toolbar.get_notification_games().click()

    def check_notification(self):
        # image_element = self.main_up_toolbar.get_image_element()
        # if image_element is False:
        #     return False
        game_notification = self.main_up_toolbar.get_element_by_app(game.THRONEWARS_ID)
        if not game_notification:
            return False
        return game_notification

    def block_page(self):
        self.get_hover(self.group_component.get_start_block_button())
        self.group_component.get_block_button().click()

    def hide_notification(self):
        self.get_hover(self.main_up_toolbar.get_element_by_app(game.THRONEWARS_ID))
        self.main_up_toolbar.get_report_notification_button().click()
        self.main_up_toolbar.get_confirm_report_notification().click()

    def update(self):
        self.main_up_toolbar.get_logo_img().click()
        #self.main_up_toolbar.get_is_logo_attached()
        # if self.main_up_toolbar.get_is_logo_attached() is True:
        #     return True

    def check_main_vertical_list(self):
        return self.main_vertical_list.get_friends()

    def go_to_group_news(self):
        self.group_component.get_groups_news_button().click()

    def open_page_by_url(self, path):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE)
        url = urlparse.urljoin(url, path)
        self.driver.get(url)
        self.driver.maximize_window()
