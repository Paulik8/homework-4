
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.group_form import GroupForm
from pages.page import Page
from constants import profiles
from components.group_component import GroupComponent
from constants import dialog


class GroupPage(Page):
    PAGE = 'group/54182734987425'

    def __init__(self, driver):
        super(GroupPage, self).__init__(driver)
        self.group_component = GroupComponent(self.driver)
        self.group_form = GroupForm(self.driver)

    def group_add(self):
        self.group_form.group_add().click()

    def group_delete(self):
        self.group_form.group_menu().click()
        self.group_form.group_delete().click()

    def is_my_group(self):
    	try:
    		self.group_form.group_menu()
    		return True
    	except TimeoutException:
    		return False

    def invite_friend(self,name):
        try:
            self.group_form.group_invite_friends().click()
            self.group_form.group_invite_search().send_keys(name)
            self.group_form.group_friend_invite().click()
            self.group_form.group_invite_button()
            return True
        except TimeoutException:
            return False


    def block_page(self):
        self.get_hover(self.group_component.get_start_block_button())
        self.group_component.get_block_button().click()

    def unblock_page(self):
        self.get_hover(self.group_component.get_start_block_button())
        self.group_component.get_unblock_button().click()

    def public_post(self):
        self.group_component.get_new_theme().click()
        self.group_component.get_message_input().send_keys(dialog.TEST_MESSAGE)
        self.group_component.get_send_button().click()

    def delete_post(self):
        self.get_hover(self.group_component.get_href_sender_item())
        self.get_hover(self.group_component.get_down_arrow())
        self.group_component.get_delete_button().click()

    def get_href_from_receiver_message(self):
        # href = self.group_component.get_href_item()
        try:
            if self.group_component.get_href_item() is False:
                return False
            return self.group_component.get_href_item().get_attribute('href')[-14:]
        except AttributeError:
            return False

    def get_href_from_sender_message(self):
        return self.group_component.get_href_sender_item().get_attribute('href')[-14:]
