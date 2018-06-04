
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.game_form import GameForm
from pages.page import Page
from constants import profiles




class GamePage(Page):
    def __init__(self, driver):
        super(GamePage, self).__init__(driver)
        self.game_form = GameForm(self.driver)
        self.PAGE = "/game/vegamix"

    def game_delete(self):
        self.game_form.game_delete().click()
        self.game_form.game_delete_repead().click()

    def game_invite_check(self, name):
        self.game_form.game_invite().click()
        try:
        	self.game_form.game_invite_name_friend(name).click()
        	self.game_form.game_invite_button()
        	return True
        except TimeoutException:
        	return False

        
