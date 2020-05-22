from selenium import webdriver

from fixture.contact_helper import ContactHelper
from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper


class Application(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def tear_down(self):
        self.driver.quit()
