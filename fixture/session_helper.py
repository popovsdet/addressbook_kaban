class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.driver.find_element_by_name("user").click()
        self.app.driver.find_element_by_name("user").clear()
        self.app.driver.find_element_by_name("user").send_keys(username)
        self.app.driver.find_element_by_name("pass").click()
        self.app.driver.find_element_by_name("pass").clear()
        self.app.driver.find_element_by_name("pass").send_keys(password)
        self.app.driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def ensure_login(self, username, password):
        if self.app.driver.find_elements_by_link_text("Logout"):
            if self.correct_username(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def correct_username(self, username):
        return self.app.driver.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    def logout(self):
        self.app.driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.app.driver.find_elements_by_link_text("Logout"):
            self.logout()
