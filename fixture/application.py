"""
Application
"""
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import Session


class Application(object):

    def __init__(self, browser, base_url):
        """
        1. Create instance of the Web Driver.
        2. Open new browser.
        3. Create instances of our classes.
        """
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.driver.implicitly_wait(1)
        self.session = Session(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        """
        Open home page
        """
        self.driver.get(self.base_url)

    def tear_down(self):
        """
        Tear down. Destroy driver
        """
        self.driver.quit()

    def is_valid(self):
        """
        Driver validation: verify that browser is exist
        :return: True if driver is exist and we can get current url otherwise False
        """
        try:
            return bool(self.driver.current_url)
        except:
            return False
