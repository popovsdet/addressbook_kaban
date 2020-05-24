"""
Application
"""
from selenium import webdriver

from fixture.contact import Contact
from fixture.group import GroupHelper
from fixture.session import Session


class Application(object):

    def __init__(self):
        """
        1. Create instance of the Web Driver.
        2. Open new browser.
        3. Create instances of our classes.
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.session = Session(self)
        self.group = GroupHelper(self)
        self.contact = Contact(self)

    def open_home_page(self):
        """
        Open home page
        """
        self.driver.get("http://localhost/addressbook/")

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
