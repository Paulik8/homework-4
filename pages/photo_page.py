import sys
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.photo_form import PhotoForm
from pages.page import Page
from constants import profiles



class PhotoPage(Page):

    def __init__(self, driver, url_user, url_photo):
        super(PhotoPage, self).__init__(driver)
        self.photo_form = PhotoForm(self.driver)
        self.PAGE = url_user + "/pphotos" + url_photo

    def add_mark_in_photo_comment(self, name):
        self.photo_form.comment_input().send_keys("@")
        try:
            self.photo_form.mark_button(name).click()
            return True
        except TimeoutException:
            return False

    def mark_in_photo_comment_blocked(self, name):
        self.photo_form.comment_input().send_keys("@" + name)
        try:
            self.photo_form.blocked_mark_button()
            return True
        except TimeoutException:
            return False