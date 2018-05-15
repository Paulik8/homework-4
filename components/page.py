import urlparse

from selenium import webdriver


class Page(object):
    BASE_URL = 'https://ok.ru'
    PAGE = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self, extra_path):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE + extra_path)
        self.driver.get(url)
        self.driver.maximize_window()

