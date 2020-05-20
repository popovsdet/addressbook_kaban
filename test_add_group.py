import unittest

from selenium import webdriver

from group import Group


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name="name_1", header="header_1", footer="footer_1"))
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        group = Group(name="", header="", footer="")
        self.create_group(group)
        self.return_to_groups_page()
        self.logout()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.driver.find_element_by_name("user").click()
        self.driver.find_element_by_name("user").clear()
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pass").click()
        self.driver.find_element_by_name("pass").clear()
        self.driver.find_element_by_name("pass").send_keys(password)
        self.driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        self.driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        self.driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        # Init group creation
        self.driver.find_element_by_name("new").click()
        # Fill group form
        self.driver.find_element_by_name("group_name").click()
        self.driver.find_element_by_name("group_name").clear()
        self.driver.find_element_by_name("group_name").send_keys(group.name)
        self.driver.find_element_by_name("group_header").click()
        self.driver.find_element_by_name("group_header").clear()
        self.driver.find_element_by_name("group_header").send_keys(group.header)
        self.driver.find_element_by_name("group_footer").click()
        self.driver.find_element_by_name("group_footer").clear()
        self.driver.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        self.driver.find_element_by_name("submit").click()

    def open_groups_page(self):
        self.driver.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
