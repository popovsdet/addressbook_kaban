class ContactHelper:
    def __init__(self, app):
        self.app = app

    def init_new_contact(self):
        self.app.driver.find_element_by_xpath('//a[text()="add new"]').click()

    def create(self, contact):
        self.init_new_contact()
        self.app.driver.find_element_by_xpath('//input[@name="firstname"]').send_keys(contact.fistname)
        self.app.driver.find_element_by_xpath('//input[@name="lastname"]').send_keys(contact.lastname)
        self.app.driver.find_element_by_xpath('//textarea[@name="address"]').send_keys(contact.address)
        self.app.driver.find_element_by_xpath('//input[@name="mobile"]').send_keys(contact.mobile)
        self.app.driver.find_element_by_xpath('//input[@name="email"]').send_keys(contact.email)
        # Submit contact
        self.app.driver.find_element_by_xpath('//input[@name="submit"]').click()
        self.goto_home_page()

    def goto_home_page(self):
        self.app.driver.find_element_by_xpath('//a[text()="home"]').click()

    def delete(self):
        self.goto_home_page()
        # Select fist contact
        self.app.driver.find_element_by_xpath('//input[@name="selected[]"]').click()
        # Click "Delete" button
        self.app.driver.find_element_by_xpath('//input[@value="Delete"]').click()
        # Close the alert
        self.app.driver.switch_to_alert().accept()
        self.goto_home_page()
