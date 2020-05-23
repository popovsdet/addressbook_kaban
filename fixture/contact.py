"""
Contacts behavior
"""


class Contact(object):
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        """
        Create a contact
        :param contact: contact object
        """
        self.init_new_contact()
        self.fill_form(contact)
        # Submit contact creation
        self.app.driver.find_element_by_xpath('//input[@name="submit"]').click()
        self.goto_home_page()

    def modify(self, contact):
        """
        Modify contact
        :param contact: contact object
        """
        self.goto_home_page()
        # Go to edit contact page
        self.app.driver.find_element_by_xpath('//img[@title="Edit"]').click()
        self.fill_form(contact)
        # Submit contact modification
        self.app.driver.find_element_by_xpath('//input[@name="update"]').click()
        self.goto_home_page()

    def delete(self):
        """
        Delete contact
        """
        self.goto_home_page()
        # Select fist contact
        self.app.driver.find_element_by_xpath('//input[@name="selected[]"]').click()
        # Click "Delete" button
        self.app.driver.find_element_by_xpath('//input[@value="Delete"]').click()
        # Close the alert
        self.app.driver.switch_to_alert().accept()
        self.goto_home_page()

    def fill_form(self, contact):
        """
        Fill contact form
        :param contact: contact object
        """
        self.change_field_value(xpath='//input[@name="firstname"]', text=contact.fistname)
        self.change_field_value(xpath='//input[@name="lastname"]', text=contact.lastname)
        self.change_field_value(xpath='//textarea[@name="address"]', text=contact.address)
        self.change_field_value(xpath='//input[@name="mobile"]', text=contact.mobile)
        self.change_field_value(xpath='//input[@name="email"]', text=contact.email)

    def init_new_contact(self):
        """
        Init new contact creation
        """
        self.app.driver.find_element_by_xpath('//a[text()="add new"]').click()

    def goto_home_page(self):
        """
        Go to home page with contact list
        """
        self.app.driver.find_element_by_xpath('//a[text()="home"]').click()

    # Common methods
    def change_field_value(self, xpath: str, text: str):
        """
        Change field value
        :param xpath: xpath
        :param text: text
        """
        if text is not None:
            self.app.driver.find_element_by_xpath(xpath).click()
            self.app.driver.find_element_by_xpath(xpath).clear()
            self.app.driver.find_element_by_xpath(xpath).send_keys(text)
