import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.games_form import GamesForm
from pages.page import Page
from constants import profiles


class GamesPage(Page):

    def __init__(self, driver, url):
        super(GamesPage, self).__init__(driver)
        self.games_form = GamesForm(self.driver)
        self.PAGE = url + "/games"

    def games_visibility(self):
        try:
            self.games_form.games_container()
            return True
        except TimeoutException:
            return False
