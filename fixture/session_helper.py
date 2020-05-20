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

    def logout(self):
        self.app.driver.find_element_by_link_text("Logout").click()
