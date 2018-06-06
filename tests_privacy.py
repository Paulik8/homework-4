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
        [name, value] = privacy_page.my_age_only_friends()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))
        
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_age_all_users_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_age_all_users()
        
        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_age_only_friends_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_age_only_friends()

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

        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_my_age_only_friends_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_age_only_friends()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()
        user_test_page.open()
        checked_age = user_test_page.age()
        self.assertNotEqual(age[0], checked_age[0])

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_my_age_all_users_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_age_all_users()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()
        user_test_page.open()
        checked_age = user_test_page.age()
        self.assertEqual(age[0], checked_age[0])

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_my_games_and_applications_only_friends_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_games_and_applications_only_friends()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)



    def test_my_games_and_applications_only_friends_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_games_and_applications_only_friends()

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

        user_test_page.open()        
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        game_page.open()
        game_page.game_delete()
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_my_games_and_applications_only_friends_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_games_and_applications_only_friends()

        game_page = GamePage(self.driver)
        game_page.open()

        auth_page = AuthPage(self.driver)
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
        game_page.open()
        game_page.game_delete()
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_games_and_applications_only_me_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_games_and_applications_only_me()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_games_and_applications_only_me_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_games_and_applications_only_me()

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
        self.assertTrue(not games_page.games_visibility())

        user_test_page.open()        
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        game_page.open()
        game_page.game_delete()
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_groups_only_me_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_groups_only_me()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_groups_only_me_chek_friends(self):
        stub_groups_only_me = u'Информация скрыта'

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_groups_only_me()

        group_page = GroupPage(self.driver)
        group_page.open()
        group_page.group_add()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        user_test_page.accept_friend()

        groups_page = GroupsPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        groups_page.open()
        checked_stub_text = groups_page.groups_container().text
        self.assertEqual(stub_groups_only_me, checked_stub_text)

        user_test_page.open()        
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        group_page.open()
        group_page.group_delete()
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_groups_all_users_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_groups_all_users()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_groups_all_users_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_groups_all_users()

        group_page = GroupPage(self.driver)
        group_page.open()
        group_page.group_add()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        groups_page = GroupsPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        groups_page.open()
        self.assertTrue(groups_page.groups_visibility())

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        group_page.open()
        group_page.group_delete()
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_subscribers_subscriptions_only_me_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_subscribers_subscriptions_only_me()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)


    def test_my_subscribers_subscriptions_only_me_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_subscribers_subscriptions_only_me()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page.open()
        user_test_page.accept_friend()

        friends_user_page = FriendsUserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        friends_user_page.open()
        self.assertTrue(not friends_user_page.subscribers_visibility())
        self.assertTrue(not friends_user_page.subscriptions_visibility())

        user_test_page.open()        
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_my_reletionship_only_friends_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_reletionship_only_friends()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)


    def test_my_reletionship_only_friends_chek_friends(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_reletionship_only_friends()

        user_43_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_43_page.open()
        name_surname = user_43_page.name_surname()
        user_43_page.add_to_friend()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_42_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_42_page.open()
        user_42_page.accept_friend()
        

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        about_page.open()
        about_page.clear_reletionship()
        about_page.add_to_reletionship(name_surname)

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open()
        main_page.accept_notification()

        user_42_page.open()
        self.assertTrue(user_42_page.reletionship_visibility())
        about_page = AboutPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        about_page.open()
        about_page.break_reletionship()
        user_42_page.open()
        user_42_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)



    def test_my_reletionship_only_friends_chek_all_users(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.my_reletionship_only_friends()

        user_43_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_43_page.open()
        name_surname = user_43_page.name_surname()
        user_43_page.add_to_friend()

        auth_page = AuthPage(self.driver)
        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_42_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_42_page.open()
        user_42_page.accept_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        about_page.open()
        about_page.clear_reletionship()
        about_page.add_to_reletionship(name_surname)

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open()
        main_page.accept_notification()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_42_page.open()
        self.assertTrue(not user_42_page.reletionship_visibility())

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)
        about_page.open()
        about_page.break_reletionship()
        user_43_page.open()
        user_43_page.del_friend()

    def test_mark_in_topics_and_comment_only_friends_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_only_friends()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_mark_in_topics_and_comment_only_friends_chek_friends_mark_in_status(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_only_friends()
        
        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        statuses_page = StatusesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        statuses_page.open()
        self.assertTrue(statuses_page.add_mark_in_status(name_surname))

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_mark_in_topics_and_comment_only_friends_chek_friends_mark_in_photo_comment(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_only_friends()
        
        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        photo_page = PhotoPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42, photos.AVATAR_URL)
        photo_page.open()
        self.assertTrue(photo_page.add_mark_in_photo_comment(name_surname))

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_mark_in_topics_and_comment_only_friends_chek_all_users_mark_in_status(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_only_friends()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        statuses_page = StatusesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK11)
        statuses_page.open()
        self.assertTrue(not statuses_page.add_mark_in_status(name_surname))

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_mark_in_topics_and_comment_only_friends_chek_all_users_mark_in_photo_comment(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_only_friends()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        photo_page = PhotoPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42, photos.AVATAR_URL)
        photo_page.open()
        self.assertTrue(not photo_page.add_mark_in_photo_comment(name))

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_mark_in_topics_and_comment_no_one_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_no_one()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_mark_in_topics_and_comment_no_one_chek_friends_mark_in_status(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_no_one()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        statuses_page = StatusesPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        statuses_page.open()
        self.assertTrue(not statuses_page.mark_in_status_blocked(name_surname))

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_mark_in_topics_and_comment_no_one_chek_friends_mark_in_photo_comment(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.mark_in_topic_no_one()
        
        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        photo_page = PhotoPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42, photos.AVATAR_URL)
        photo_page.open()
        self.assertTrue(not photo_page.mark_in_photo_comment_blocked(name_surname))

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)        

    def test_games_invite_only_friends_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.game_invite_only_friends()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_games_invite_only_friends_chek_friends(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.game_invite_only_friends()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        game_page = GamePage(self.driver)
        game_page.open()
        self.assertTrue(game_page.game_invite_check(name_surname))

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_games_invite_only_friends_chek_all_users(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.game_invite_only_friends()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        game_page = GamePage(self.driver)
        game_page.open()
        self.assertTrue(not game_page.game_invite_check(name_surname))

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)


    def test_games_invite_no_one_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.game_invite_no_one()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_games_invite_no_one_chek_friends(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.game_invite_no_one()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        game_page = GamePage(self.driver)
        game_page.open()
        self.assertTrue(not game_page.game_invite_check(name_surname))

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)

    def test_group_invite_no_one_radiobutton_clicked(self):
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.group_invite_no_one()

        privacy_page.open()
        self.assertTrue(privacy_page.is_cheked_element(name, value))

        privacy_page.set_radiobutton_initial_value(name, value)

    def test_group_invite_no_one_chek_friends(self):
        auth_page = AuthPage(self.driver)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        [name, value] = privacy_page.group_invite_no_one()

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        name_surname = user_test_page.name_surname()
        user_test_page.accept_friend()

        group_page = GroupPage(self.driver)
        group_page.open()
        group_page.group_add()
        self.assertTrue(not group_page.invite_friend(name_surname))

        group_page.open()
        group_page.group_delete()

        user_test_page.open()
        user_test_page.del_friend()

        auth_page.logout()
        auth_page.re_login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page.open()
        privacy_page.set_radiobutton_initial_value(name, value)
