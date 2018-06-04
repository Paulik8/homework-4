# -*- coding: utf-8 -*-
import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles
from constants import photos
from pages.auth_page import AuthPage
from pages.privacy_page import PrivacyPage
from pages.friends_user_page import FriendsUserPage
from pages.main_page import MainPage
from pages.user_page import UserPage
from pages.games_page import GamesPage
from pages.game_page import GamePage
from pages.groups_page import GroupsPage
from pages.group_page import GroupPage
from pages.about_page import AboutPage
from pages.statuses_page import StatusesPage
from pages.photo_page import PhotoPage


class TestsPrivacy(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', profiles.BROWSER)

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_my_age_only_friends_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_age_only_friends()

        privacy_page.open()
        assertTrue(privacy_page.is_cheked_element(radiobutton))
        
        privacy_page.set_radiobutton_initial_value(radiobutton)

    def test_my_age_all_users_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_age_all_users()

        privacy_page.open()
        assertTrue(privacy_page.is_cheked_element(radiobutton))

        privacy_page.set_radiobutton_initial_value(radiobutton)

    def test_my_age_only_friends_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_age_only_friends()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        user_test_page.accept_friend()
        user_test_page.open()
        checked_age = user_test_page.age()
        self.assertEqual(age[0], checked_age[0])

        user_test_page.del_friend()
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(radiobutton)


    def test_my_age_only_friends_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_age_only_friends()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()
        user_test_page.open()
        checked_age = user_test_page.age()
        self.assertNotEqual(age[0], checked_age[0])

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(radiobutton)


    def test_my_age_all_users_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_age_all_users()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()
        user_test_page.open()
        checked_age = user_test_page.age()
        self.assertNotEqual(age[0], checked_age[0])

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(radiobutton)


    def test_my_games_and_applications_only_friends_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_games_and_applications_only_friends()

        privacy_page.open()
        assertTrue(privacy_page.is_cheked_element(radiobutton))

        privacy_page.set_radiobutton_initial_value(radiobutton)



    def test_my_games_and_applications_only_friends_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_games_and_applications_only_friends()

        game_page = GamePage(self.driver)
        game_page.open()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        user_test_page.accept_friend()

        games_page = GamesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        games_page.open()
        self.assertTrue(games_page.games_visibility())

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()        
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        game_page = GamePage(self.driver)
        game_page.open()
        game_page.game_delete()
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(radiobutton)


    def test_my_games_and_applications_only_friends_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        radiobutton = privacy_page.my_games_and_applications_only_friends()

        game_page = GamePage(self.driver)
        game_page.open()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        games_page = GamesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        games_page.open()
        self.assertTrue(not games_page.games_visibility())

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        game_page = GamePage(self.driver)
        game_page.open()
        game_page.game_delete()
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(radiobutton)


    # def test_my_games_and_applications_only_me(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.my_games_and_applications_only_me()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.my_games_and_applications_only_friends())
    #         privacy_page.click(privacy_page.my_games_and_applications_only_me())
    #     else:
    #         privacy_page.click(privacy_page.my_games_and_applications_only_me())
       
    #     privacy_page.click(privacy_page.save())


    #     game_page = GamePage(self.driver)
    #     game_page.open()

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     user_test_page.accept_friend()

    #     games_page = GamesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     games_page.open()
    #     self.assertTrue(not games_page.games_visibility())

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()        
    #     user_test_page.del_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     game_page = GamePage(self.driver)
    #     game_page.open()
    #     game_page.game_delete()
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    # def test_my_groups_only_me(self):
    #     stub_groups_only_me = u'Информация скрыта'

    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.my_groups_only_me()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.my_groups_all_users())
    #         privacy_page.click(privacy_page.my_groups_only_me())
    #     else:
    #         privacy_page.click(privacy_page.my_groups_only_me())
       
    #     privacy_page.click(privacy_page.save())


    #     group_page = GroupPage(self.driver)
    #     group_page.open()
    #     if group_page.is_my_group() == True:
    #         pass
    #     else:
    #         group_page.group_add()

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     user_test_page.accept_friend()

    #     groups_page = GroupsPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     groups_page.open()
    #     checked_stub_text = groups_page.groups_container().text
    #     self.assertEqual(stub_groups_only_me, checked_stub_text)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()        
    #     user_test_page.del_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     group_page = GroupPage(self.driver)
    #     group_page.open()
    #     group_page.group_delete()
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    # def test_my_groups_all_users(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.my_groups_all_users()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.my_groups_only_me())
    #         privacy_page.click(privacy_page.my_groups_all_users())
    #     else:
    #         privacy_page.click(privacy_page.my_groups_all_users())
       
    #     privacy_page.click(privacy_page.save())


    #     group_page = GroupPage(self.driver)
    #     group_page.open()
    #     if group_page.is_my_group() == True:
    #         pass
    #     else:
    #         group_page.group_add()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)


    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     if user_test_page.is_friend() == True:
    #         user_test_page.del_friend()

    #     groups_page = GroupsPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     groups_page.open()
    #     self.assertTrue(groups_page.groups_visibility())

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     group_page = GroupPage(self.driver)
    #     group_page.open()
    #     group_page.group_delete()
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    # def test_my_subscribers_subscriptions_only_me(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.my_subscribers_subscriptions_only_me()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.my_subscribers_subscriptions_all_users())
    #         privacy_page.click(privacy_page.my_subscribers_subscriptions_only_me())
    #     else:
    #         privacy_page.click(privacy_page.my_subscribers_subscriptions_only_me())
       
    #     privacy_page.click(privacy_page.save())

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     if user_test_page.is_friend() == True:
    #         user_test_page.del_friend()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     if user_test_page.is_friend() == True:
    #         user_test_page.del_friend()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     friends_user_page = FriendsUserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     friends_user_page.open()
    #     self.assertTrue(not friends_user_page.subscribers_visibility())
    #     self.assertTrue(not friends_user_page.subscriptions_visibility())

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    # def test_my_reletionship_only_friends(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.my_reletionship_only_friends()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.my_reletionship_all_users())
    #         privacy_page.click(privacy_page.my_reletionship_only_friends())
    #     else:
    #         privacy_page.click(privacy_page.my_reletionship_only_friends())
       
    #     privacy_page.click(privacy_page.save())


    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     name = user_test_page.name_surname()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     user_test_page.accept_friend()
        

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     about_page = AboutPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     about_page.open()
    #     about_page.clear_reletionship()
    #     about_page.add_to_reletionship(name)


    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     main_page.accept_notification()

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_page.open()
    #     self.assertTrue(user_page.reletionship_visibility())


    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_page.open()
    #     self.assertTrue(not user_page.reletionship_visibility())

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    #     about_page = AboutPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     about_page.open()
    #     about_page.break_reletionship()

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_page.open()
    #     user_page.del_friend()

    # def test_mark_in_topics_and_comment_only_friends(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.mark_in_topic_only_friends()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.mark_in_topic_no_one())
    #         privacy_page.click(privacy_page.mark_in_topic_only_friends())
    #     else:
    #         privacy_page.click(privacy_page.mark_in_topic_only_friends())
       
    #     privacy_page.click(privacy_page.save())
        
    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)


    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     name = user_test_page.name_surname()
    #     user_test_page.accept_friend()

    #     statuses_page = StatusesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     statuses_page.open()
    #     self.assertTrue(statuses_page.add_mark_in_status(name))

    #     photo_page = PhotoPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42, photos.AVATAR_URL)
    #     photo_page.open()
    #     self.assertTrue(photo_page.add_mark_in_photo_comment(name))


    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)


    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     if user_test_page.is_friend() == True:
    #         user_test_page.del_friend()

    #     statuses_page = StatusesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK11)
    #     statuses_page.open()
    #     self.assertTrue(not statuses_page.add_mark_in_status(name))

    #     photo_page = PhotoPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42, photos.AVATAR_URL)
    #     photo_page.open()
    #     self.assertTrue(not photo_page.add_mark_in_photo_comment(name))

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_page.open()
    #     user_page.del_friend()

    # def test_mark_in_topics_and_comment_no_one(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.mark_in_topic_no_one()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.mark_in_topic_only_friends())
    #         privacy_page.click(privacy_page.mark_in_topic_no_one())
    #     else:
    #         privacy_page.click(privacy_page.mark_in_topic_no_one())
       
    #     privacy_page.click(privacy_page.save())
        
    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     name = user_test_page.name()[0]
    #     user_test_page.accept_friend()

    #     statuses_page = StatusesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     statuses_page.open()
    #     self.assertTrue(statuses_page.mark_in_status_blocked(name))

    #     photo_page = PhotoPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42, photos.AVATAR_URL)
    #     photo_page.open()
    #     self.assertTrue(photo_page.mark_in_photo_comment_blocked(name))


    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_page.open()
    #     user_page.del_friend()


    # def test_games_invite_only_friends(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.game_invite_only_friends()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.game_invite_no_one())
    #         privacy_page.click(privacy_page.game_invite_only_friends())
    #     else:
    #         privacy_page.click(privacy_page.game_invite_only_friends())
       
    #     privacy_page.click(privacy_page.save())
        
    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     name = user_test_page.name_surname()
    #     user_test_page.accept_friend()

    #     game_page = GamePage(self.driver)
    #     game_page.open()
    #     self.assertTrue(game_page.game_invite_check(name))

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     if user_test_page.is_friend() == True:
    #         user_test_page.del_friend()


    #     game_page = GamePage(self.driver)
    #     game_page.open()
    #     self.assertTrue(not game_page.game_invite_check(name))

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_page.open()
    #     user_page.del_friend()


    # def test_games_invite_no_one(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.game_invite_no_one()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.game_invite_only_friends())
    #         privacy_page.click(privacy_page.game_invite_no_one())
    #     else:
    #         privacy_page.click(privacy_page.game_invite_no_one())
       
    #     privacy_page.click(privacy_page.save())
        
    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     name = user_test_page.name_surname()
    #     user_test_page.accept_friend()

    #     game_page = GamePage(self.driver)
    #     game_page.open()
    #     self.assertTrue(not game_page.game_invite_check(name))

    #     auth_page.logout()
        
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_page.open()
    #     user_page.del_friend()


    # def test_group_invite_no_one(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()

    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()

    #     initial_checked_radiobutton = privacy_page.group_invite_no_one()
    #     initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
    #     initial_checked_radiobutton_name = initial_checked_radiobutton.get_attribute("name")

    #     if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(privacy_page.group_invite_only_friends())
    #         privacy_page.click(privacy_page.group_invite_no_one())
    #     else:
    #         privacy_page.click(privacy_page.group_invite_no_one())
       
    #     privacy_page.click(privacy_page.save())
        
    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_test_page.open()
    #     user_test_page.add_to_friend()

    #     auth_page.logout()
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

    #     user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
    #     user_test_page.open()
    #     name = user_test_page.name_surname()
    #     user_test_page.accept_friend()

    #     group_page = GroupPage(self.driver)
    #     group_page.open()
    #     if group_page.is_my_group() is not True:
    #         group_page.group_add()
    #     self.assertTrue(not group_page.invite_friend(name))

    #     group_page = GroupPage(self.driver)
    #     group_page.open()
    #     group_page.group_delete()

    #     auth_page.logout()
        
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
    #     privacy_page = PrivacyPage(self.driver)
    #     privacy_page.open()
    #     initial_checked_radiobutton = privacy_page.set_radiobutton_by_value(initial_checked_radiobutton_name, initial_checked_radiobutton_value)
    #     if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
    #         privacy_page.click(initial_checked_radiobutton)
    #         privacy_page.click(privacy_page.save())

    #     user_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
    #     user_page.open()
    #     user_page.del_friend()