from selenium import webdriver


class Application(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
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
        self.open_groups_page()
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
        self.return_to_groups_page()

    def open_groups_page(self):
        self.driver.find_element_by_link_text("groups").click()

    def tear_down(self):
        self.driver.quit()

    def init_new_contact(self):
        self.driver.find_element_by_xpath('//a[text()="add new"]').click()

    def create_contact(self, contact):
        self.init_new_contact()
        self.driver.find_element_by_xpath('//input[@name="firstname"]').send_keys(contact.fistname)
        self.driver.find_element_by_xpath('//input[@name="lastname"]').send_keys(contact.lastname)
        self.driver.find_element_by_xpath('//textarea[@name="address"]').send_keys(contact.address)
        self.driver.find_element_by_xpath('//input[@name="mobile"]').send_keys(contact.mobile)
        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys(contact.email)
        # Submit contact
        self.driver.find_element_by_xpath('//input[@name="submit"]').click()
        self.goto_home_page()

    def goto_home_page(self):
        self.driver.find_element_by_xpath('//a[text()="home"]').click()
