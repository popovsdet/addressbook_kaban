import mysql.connector

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_groups(self) -> list:
        """
        Get list of groups from DB
        :return: list
        """
        db_group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                db_group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return db_group_list

    def get_contacts(self) -> list:
        """
        Get  list of contacts from DB
        :return: list
        """
        db_contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                db_contact_list.append(Contact(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return db_contact_list

    def tear_down(self):
        """
        Close connection
        """
        self.connection.close()
