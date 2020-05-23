"""
Session behavior
"""


class Session(object):
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        """
        Login
        :param username: username
        :param password: password
        """
        self.app.open_home_page()
        self.app.driver.find_element_by_name("user").click()
        self.app.driver.find_element_by_name("user").clear()
        self.app.driver.find_element_by_name("user").send_keys(username)
        self.app.driver.find_element_by_name("pass").click()
        self.app.driver.find_element_by_name("pass").clear()
        self.app.driver.find_element_by_name("pass").send_keys(password)
        self.app.driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def ensure_login(self, username, password):
        """
        Verify login with correct username and login it necessary
        :param username: username
        :param password: password
        """
        # When we login there is "Logout" button on the page
        if self.app.driver.find_elements_by_link_text("Logout"):
            # If username isn't correct ...
            if self.correct_username(username):
                return
            else:
                # ... we logout and ...
                self.logout()
        # ... login again
        self.login(username, password)

    def correct_username(self, username):
        """
        Compare expected and actual username
        :param username: username
        :return: True if "username" present on the page, otherwise False
        """
        return self.app.driver.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    def logout(self):
        """
        Click "Logout" button on the page
        """
        self.app.driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        """
        Verify text "Logout" on the page and logout
        """
        if self.app.driver.find_elements_by_link_text("Logout"):
            self.logout()
