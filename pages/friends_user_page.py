from components.friends_list import FriendsList
from pages.page import Page
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class FriendsUserPage(Page):

	def __init__(self, driver, user_url):
		super(FriendsUserPage, self).__init__(driver)
		self.user_url = user_url
		self.PAGE = user_url + '/friends'

	def subscribers_visibility(self):
		try:
			friends_list = FriendsList(self.driver)
			friends_list.subscribers_list(self.user_url)
			return True
		except TimeoutException:
			return False    

	def subscriptions_visibility(self):
		try:
			friends_list = FriendsList(self.driver)
			friends_list.subscriptions_list(self.user_url)
			return True
		except TimeoutException:
			return False  
