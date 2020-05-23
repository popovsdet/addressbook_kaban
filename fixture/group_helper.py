class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        if not (self.app.driver.current_url.endswith("/group.php") and
                self.app.driver.find_elements_by_name("new")):
            self.app.driver.find_element_by_link_text("group page").click()

    def create(self, group):
        self.open_groups_page()
        # Init group creation
        self.app.driver.find_element_by_name("new").click()
        self.fill(group)
        # Submit group creation
        self.app.driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify(self, group):
        self.open_groups_page()
        self.select_fist_group()
        # Click "Edit" button
        self.app.driver.find_element_by_xpath('//input[@name="edit"]').click()
        self.fill(group)
        # Submit modification
        self.app.driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.app.driver.find_element_by_link_text("groups").click()

    def delete(self):
        self.open_groups_page()
        self.select_fist_group()
        # submit deletion
        self.app.driver.find_element_by_xpath('//input[@name="delete"]').click()
        self.return_to_groups_page()

    def select_fist_group(self):
        self.app.driver.find_element_by_xpath('//input[@name="selected[]"]').click()

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element_by_name(field_name).click()
            self.app.driver.find_element_by_name(field_name).clear()
            self.app.driver.find_element_by_name(field_name).send_keys(text)

    def fill(self, group):
        """
        Fill group form
        :param group: group object
        """
        self.change_field_value(field_name="group_name", text=group.name)
        self.change_field_value(field_name="group_header", text=group.header)
        self.change_field_value(field_name="group_footer", text=group.footer)

    def number(self):
        self.open_groups_page()
        return len(self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]'))
