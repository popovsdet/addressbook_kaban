class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        self.app.driver.find_element_by_link_text("group page").click()

    def create(self, group):
        self.open_groups_page()
        # Init group creation
        self.app.driver.find_element_by_name("new").click()
        # Fill group form
        self.app.driver.find_element_by_name("group_name").click()
        self.app.driver.find_element_by_name("group_name").clear()
        self.app.driver.find_element_by_name("group_name").send_keys(group.name)
        self.app.driver.find_element_by_name("group_header").click()
        self.app.driver.find_element_by_name("group_header").clear()
        self.app.driver.find_element_by_name("group_header").send_keys(group.header)
        self.app.driver.find_element_by_name("group_footer").click()
        self.app.driver.find_element_by_name("group_footer").clear()
        self.app.driver.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        self.app.driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.app.driver.find_element_by_link_text("groups").click()

    def delete(self):
        self.open_groups_page()
        # select firs group
        self.app.driver.find_element_by_xpath('//input[@name="selected[]"]').click()
        # submit deletion
        self.app.driver.find_element_by_xpath('//input[@name="delete"]').click()
        self.return_to_groups_page()
