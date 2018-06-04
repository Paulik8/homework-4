
from pages.page import Page
from components.privacy_component import PrivacyForm


class PrivacyPage(Page):

	def __init__(self, driver):
		super(PrivacyPage, self).__init__(driver)
		self.privacy_component = PrivacyForm(self.driver)
		self.PAGE = '/settings/privacy'

	def radiobutton_click(self, name, value):
		initial_checked_radiobutton = self.privacy_component.get_radiobutton_by_name_and_value(name, value)
		if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
			if(initial_checked_radiobutton.get_attribute("value") == 0):
				self.privacy_component.get_radiobutton_by_name_and_value(name, self.privacy_component.NO_ONE).click()
			else:
				self.privacy_component.get_radiobutton_by_name_and_value(name, self.privacy_component.ALL_USERS).click()
			self.privacy_component.get_radiobutton_by_name_and_value(name, value).click()
		else:
			self.privacy_component.get_radiobutton_by_name_and_value(name, value).click()
		self.click(self.save())
		return initial_checked_radiobutton

	def set_radiobutton_initial_value(self, radiobutton):
		if(self.is_cheked_element(radiobutton) == false):
			self.click(radiobutton)
 			self.click(self.save())

	def my_age_only_friends(self):
		return self.radiobutton_click(self.privacy_component.MY_AGE, self.privacy_component.ONLY_FRIENDS)

	def my_age_all_users(self):
		return self.radiobutton_click(self.privacy_component.MY_AGE, self.privacy_component.ALL_USERS)


	def my_games_and_applications_only_friends(self):
		return self.radiobutton_click(self.privacy_component.MY_GAMES_AND_APPLICATIONS, self.privacy_component.ONLY_FRIENDS)

	def my_games_and_applications_only_me(self):
		return self.radiobutton_click(self.privacy_component.MY_GAMES_AND_APPLICATIONS, self.privacy_component.NO_ONE)						

	def my_groups_all_users(self):
		return self.radiobutton_click(self.privacy_component.MY_GROUPS, self.privacy_component.ALL_USERS)

	def my_groups_only_me(self):
		return self.radiobutton_click(self.privacy_component.MY_GROUPS, self.privacy_component.NO_ONE)						

	def my_subscribers_subscriptions_all_users(self):
		return self.radiobutton_click(self.privacy_component.MY_SUBSCRIBERS_SUBSCRIPTIONS, self.privacy_component.ALL_USERS)

	def my_subscribers_subscriptions_only_me(self):
		return self.radiobutton_click(self.privacy_component.MY_SUBSCRIBERS_SUBSCRIPTIONS, self.privacy_component.NO_ONE)						

	def my_reletionship_all_users(self):
		return self.radiobutton_click(self.privacy_component.MY_RELETIONSHIP, self.privacy_component.ALL_USERS)

	def my_reletionship_only_friends(self):
		return self.radiobutton_click(self.privacy_component.MY_RELETIONSHIP, self.privacy_component.ONLY_FRIENDS)													

	def group_invite_no_one(self):
		return self.radiobutton_click(self.privacy_component.GROUPS_INVITE, self.privacy_component.NO_ONE)

	def group_invite_only_friends(self):
		return self.radiobutton_click(self.privacy_component.GROUPS_INVITE, self.privacy_component.ONLY_FRIENDS)						

	def game_invite_no_one(self):
		return self.radiobutton_click(self.privacy_component.GAMES_INVITE, self.privacy_component.NO_ONE)

	def game_invite_only_friends(self):
		return self.radiobutton_click(self.privacy_component.GAMES_INVITE, self.privacy_component.ONLY_FRIENDS)

	def mark_in_topic_no_one(self):
		return self.radiobutton_click(self.privacy_component.MARK_IN_TOPIC, self.privacy_component.NO_ONE)

	def mark_in_topic_only_friends(self):
		return self.radiobutton_click(self.privacy_component.MARK_IN_TOPIC, self.privacy_component.ONLY_FRIENDS)								

	def set_radiobutton_by_value(self, name, value):
		return self.privacy_component.get_radiobutton_by_name_and_value("@name = '"+ name + "'", "@value = '"+ value + "'")

	def save(self):
		return self.privacy_component.get_save_button()

	def is_cheked_element(self, radiobutton):
		if radiobutton.get_attribute("checked") is not None:
			return true
		else:
			return false

	def click(self, radiobutton):
		self.driver.execute_script("arguments[0].click();", radiobutton)
		
