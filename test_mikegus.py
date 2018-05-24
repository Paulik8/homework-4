# -*- coding: utf-8 -*-

import unittest
import os
from pages.about_page import AboutPage
from pages.auth_page import AuthPage
from pages.community_page import CommunityPage
from pages.main_page import MainPage
from constants import profiles
from constants import army
from constants import career
from constants import comminity
from constants import study
from constants import main_page

from selenium.common.exceptions import NoSuchElementException

from pages.base_settings_page import BaseSettingsPage

from selenium.webdriver import DesiredCapabilities, Remote


class TestsMikeGus(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_change_sex(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()

        personal_data.check_female()
        personal_data.save()
        personal_data.close_save()

        personal_data = base_settings_page.personal_data()
        self.assertEqual(personal_data.is_female(), True)
        self.assertEqual(personal_data.is_male(), False)

        m_page = MainPage(self.driver)
        m_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)
        self.assertEqual(m_page.my_birth_note(), main_page.FEMALE_BIRTH_NOTE)

        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.check_male()
        personal_data.save()
        personal_data.close_save()

        personal_data = base_settings_page.personal_data()
        self.assertEqual(personal_data.is_female(), False)
        self.assertEqual(personal_data.is_male(), True)

        m_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)
        self.assertEqual(m_page.my_birth_note(), main_page.MALE_BIRTH_NOTE)

    def test_army_correct_city_unit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.add_city_unit(army.CORRECT_CITY, army.CORRECT_UNIT)
        army_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_unit()
        except NoSuchElementException:
            self.fail('в/ч не добавлена')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(army.CORRECT_ARMY_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_army_no_city_correct_unit(self):

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.add_city_unit('', army.CORRECT_UNIT)
        army_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_unit()
        except NoSuchElementException:
            self.fail('в/ч не добавлена')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(army.CORRECT_ARMY_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_army_incorrect_city_unit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open_page_by_url('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.put_city(army.CORRECT_CITY)
        army_form.put_unit(army.INCORRECT_UNIT)

        error = army_form.army_error()
        self.assertEqual(error, army.ERROR_INVALID_UNIT)

        army_form.add_city_unit(army.INCORRECT_CITY, army.CORRECT_UNIT)
        army_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_unit()
        except NoSuchElementException:
            self.fail('в/ч не добавлена')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(army.CORRECT_ARMY_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_army_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.add_city_unit(army.CORRECT_CITY, army.CORRECT_UNIT)
        army_form.button_ok()
        about_form.close_popup()

        army_form = about_form.army_form()
        army_form.add_city_unit(army.CORRECT_CITY, army.CORRECT_UNIT)
        error = army_form.army_error()
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(army.CORRECT_ARMY_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_career_correct_city_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.add_city_job(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        career_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_job()
        except NoSuchElementException:
            self.fail('место работы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(career.CORRECT_CAREER_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_career_no_city_correct_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.put_city('')
        career_form.add_job(career.CORRECT_JOB)
        career_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_job()
        except NoSuchElementException:
            self.fail('место работы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(career.CORRECT_CAREER_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_career_incorrect_city_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.put_city(career.INCORRECT_CITY_COUNTRY)
        error = career_form.city_error()
        self.assertEqual(error, career.ERROR_INVALID_CITY)

        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)
        about_form = about_page.about_form()
        career_form = about_form.career_form()

        career_form.add_city(career.CORRECT_CITY_COUNTRY)
        career_form.put_job(career.INCORRECT_JOB)
        error = career_form.job_error()
        self.assertEqual(error, career.ERROR_INVALID_JOB)

        career_form.put_job('')
        career_form.put_city(career.INCORRECT_CITY_COUNTRY)
        error = career_form.city_error()
        self.assertEqual(error, career.ERROR_INVALID_CITY)

    def test_career_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.add_city_job(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        career_form.button_ok()
        about_form.close_popup()

        career_form = about_form.career_form()
        career_form.add_city_job(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        error = career_form.job_error()
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(career.CORRECT_CAREER_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_study_correct_city_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.add_city_school(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        study_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_school()
        except NoSuchElementException:
            self.fail('место учебы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(study.CORRECT_SCHOOL_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_study_no_city_correct_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.put_city('')
        study_form.add_school(study.CORRECT_SCHOOL)
        study_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_school()
        except NoSuchElementException:
            self.fail('место учебы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(study.CORRECT_SCHOOL_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_study_incorrect_city_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.put_city(study.INCORRECT_CITY_COUNTRY)
        error = study_form.city_error()
        self.assertEqual(error, study.ERROR_INVALID_CITY)

        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)
        about_form = about_page.about_form()
        study_form = about_form.study_form()

        study_form.add_city(study.CORRECT_CITY_COUNTRY)
        study_form.put_school(study.INCORRECT_SCHOOL)
        error = study_form.school_error()
        self.assertEqual(error, study.ERROR_INVALID_SCHOOL)

        study_form.put_school('')
        study_form.put_city(study.INCORRECT_CITY_COUNTRY)
        error = study_form.city_error()
        self.assertEqual(error, study.ERROR_INVALID_CITY)

    def test_school_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.add_city_school(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        study_form.button_ok()
        about_form.close_popup()

        study_form = about_form.study_form()
        study_form.add_city_school(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        error = study_form.school_error()
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver)
        community_page.open_page_by_url(study.CORRECT_SCHOOL_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()