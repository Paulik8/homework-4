import sys
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.statuses_form import StatusesForm
from pages.page import Page
from constants import profiles



class StatusesPage(Page):

    def __init__(self, driver, url):
        super(StatusesPage, self).__init__(driver)
        self.statuses_form = StatusesForm(self.driver)
        self.PAGE = url + "/statuses"

    def add_mark_in_status(self, name):
        self.statuses_form.input_status_placeholder().click()
        self.statuses_form.input_status_posting_placeholder().send_keys("@")
        try:
            self.statuses_form.mark_button(name).click()
            return True
        except TimeoutException:
            return False

    def mark_in_status_blocked(self, name):
        self.statuses_form.input_status_placeholder().click()
        self.statuses_form.input_status_posting_placeholder().send_keys("@" + name)
        try:
            self.statuses_form.blocked_mark_button()
            return True
        except TimeoutException:
            return False
