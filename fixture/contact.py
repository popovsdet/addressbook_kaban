"""
Contacts behavior
"""
import re

from model.contact import Contact


class ContactHelper(object):
    contact_list_cache = None

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
        self.contact_list_cache = None

    def modify(self, contact, index):
        """
        Modify contact
        :param contact: contact object
        """
        self.goto_home_page()
        # Go to edit contact page
        self.open_edit_page(index)
        self.fill_form(contact)
        # Submit contact modification
        self.app.driver.find_element_by_xpath('//input[@name="update"]').click()
        self.goto_home_page()
        self.contact_list_cache = None

    def delete(self, index):
        """
        Delete contact
        """
        self.goto_home_page()
        # Select fist contact
        self.select(index)
        # Click "Delete" button
        self.app.driver.find_element_by_xpath('//input[@value="Delete"]').click()
        # Close the alert
        self.app.driver.switch_to.alert.accept()
        self.goto_home_page()
        self.contact_list_cache = None

    def select(self, index):
        self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]')[index].click()

    def open_edit_page(self, index):
        self.goto_home_page()
        self.app.driver.find_elements_by_xpath('//img[@title="Edit"]')[index].click()

    def get_contact_from_edit_page(self, index):
        self.open_edit_page(index)
        first_name = self.app.driver.find_element_by_xpath('//input[@name="firstname"]').get_attribute('value')
        last_name = self.app.driver.find_element_by_xpath('//input[@name="lastname"]').get_attribute('value')
        id = self.app.driver.find_element_by_xpath('//input[@name="id"]').get_attribute('value')
        home_phone = self.app.driver.find_element_by_xpath('//input[@name="home"]').get_attribute('value')
        work_phone = self.app.driver.find_element_by_xpath('//input[@name="work"]').get_attribute('value')
        mobile_phone = self.app.driver.find_element_by_xpath('//input[@name="mobile"]').get_attribute('value')
        secondary_phone = self.app.driver.find_element_by_xpath('//input[@name="phone2"]').get_attribute('value')
        return Contact(first_name=first_name, last_name=last_name, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def open_view_page(self, index):
        self.goto_home_page()
        self.app.driver.find_elements_by_xpath('//img[@title="Details"]')[index].click()

    def get_contact_from_view_page(self, index):
        self.open_view_page(index)
        text = self.app.driver.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def fill_form(self, contact):
        """
        Fill contact form
        :param contact: contact object
        """
        self.change_field_value(xpath='//input[@name="firstname"]', text=contact.first_name)
        self.change_field_value(xpath='//input[@name="lastname"]', text=contact.last_name)
        self.change_field_value(xpath='//textarea[@name="address"]', text=contact.address)
        self.change_field_value(xpath='//input[@name="mobile"]', text=contact.mobile_phone)
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
        if not self.app.driver.current_url.endswith("addressbook/"):
            self.app.driver.find_element_by_xpath('//a[text()="home"]').click()

    def count(self):
        """
        Number of groups on the page
        """
        self.goto_home_page()
        return len(self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]'))

    def get_contact_list(self):
        if self.contact_list_cache is None:
            self.goto_home_page()
            self.contact_list_cache = []
            rows = self.app.driver.find_elements_by_xpath('//tr[@name="entry"]')
            for row in rows:
                cells = row.find_elements_by_xpath('td')
                fist_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_xpath('input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_list_cache.append(
                    Contact(first_name=fist_name, last_name=last_name, id=id, all_phones_home_page=all_phones))

        # Return copy of cache using list()
        return list(self.contact_list_cache)

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
