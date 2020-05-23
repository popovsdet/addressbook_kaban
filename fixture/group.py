"""
Groups behavior
"""


class Group(object):
    def __init__(self, app):
        """
        Init group's object
        :param app: app_fixture
        """
        self.app = app

    def create(self, group):
        """
        Create group
        :param group: group object
        """
        self.open_groups_page()
        # Init group creation
        self.app.driver.find_element_by_name("new").click()
        self.fill(group)
        # Submit group creation
        self.app.driver.find_element_by_name("submit").click()
        self.open_groups_page()

    def modify(self, group):
        """
        Modify group
        :param group: group object
        """
        self.open_groups_page()
        self.select_first_group()
        # Click "Edit" button
        self.app.driver.find_element_by_xpath('//input[@name="edit"]').click()
        self.fill(group)
        # Submit modification
        self.app.driver.find_element_by_name("update").click()
        self.open_groups_page()

    def delete(self):
        """
        Delete group
        """
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        self.app.driver.find_element_by_xpath('//input[@name="delete"]').click()
        self.open_groups_page()

    def select_first_group(self):
        """
        Select first group
        """
        self.app.driver.find_element_by_xpath('//input[@name="selected[]"]').click()

    def fill(self, group):
        """
        Fill group form
        :param group: group object
        """
        self.change_field_value(field_name="group_name", text=group.name)
        self.change_field_value(field_name="group_header", text=group.header)
        self.change_field_value(field_name="group_footer", text=group.footer)

    def number(self):
        """
        Number of groups on the page
        """
        self.open_groups_page()
        return len(self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]'))

    def open_groups_page(self):
        """
        Button
        Open groups page
        """
        if not (self.app.driver.current_url.endswith("/group.php") and
                self.app.driver.find_elements_by_name("new")):
            self.app.driver.find_element_by_link_text("groups").click()

    # Common methods
    def change_field_value(self, field_name, text):
        """
        Change field value
        :param field_name: attribute "name" in the web element
        :param text: text
        """
        if text is not None:
            self.app.driver.find_element_by_name(field_name).click()
            self.app.driver.find_element_by_name(field_name).clear()
            self.app.driver.find_element_by_name(field_name).send_keys(text)
