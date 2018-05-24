# -*- coding: utf-8 -*-
from components.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class UserForm(BaseComponent):
    BUTTON_REQUEST_SENT = "//span[@class='dropdown_ac button-pro __sec __with-arrow']"
    BUTTON_ADD_TO_FRIENDS = "//span[@class='dropdown_ac button-pro __wide']"
    BUTTON_ACCEPT_FRIEND_REQUEST = "//a[@class='dropdown_ac button-pro']"
    BUTTON_FRIENDS = "//span[@class='dropdown_ac button-pro __sec __with-arrow' and text()='Друзья']"
    BUTTON_FRIENDS_CONTROL_MENU = "//span[@class='dropdown_ac button-pro __sec']"
    BUTTON_DEL_FRIEND = "//div[@class='dropdown_ic ic_delete']"
    MY_AGE = "//div[@data-type='AGE']"
    RELATIONSHIP = "//a[@class='o user-profile_i_relation-t']"
    BUTTON_EXPEND_ITEM = "//li[@id='action_menu_expand_item']"
    BUTTON_SEND_GROUPS = "//i[@class='tico_img ic ic_group']"
    USER_NAME = "//h1[@class='mctc_name_tx bl']"

    def sent_request_add_to_friends(self):
        return self.get_element_by_path(self.BUTTON_ADD_TO_FRIENDS)

    def accept_friend_request(self):
        return self.get_element_by_path(self.BUTTON_ACCEPT_FRIEND_REQUEST)

    def button_menu_friends(self):
        return self.get_clickable_element(self.BUTTON_FRIENDS_CONTROL_MENU)

    def button_del_friend(self):
        return self.get_clickable_element(self.BUTTON_DEL_FRIEND)       

    def is_friend(self):
        try:
            self.get_element_by_path(self.BUTTON_FRIENDS)
            return True
        except TimeoutException:
            return False

    def age(self):
        return self.get_element_by_path(self.MY_AGE)

    def relationship(self):
        return self.get_element_by_path(self.RELATIONSHIP)

    def extend_item(self):
        return self.get_element_by_path(self.BUTTON_EXPEND_ITEM)

    def send_groups(self):
        return self.get_element_by_path(self.BUTTON_SEND_GROUPS)
    
    def name(self):
        return self.get_element_by_path(self.USER_NAME)      

