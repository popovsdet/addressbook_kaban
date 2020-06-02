import mysql.connector

from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=self.host, database=self.name, user=self.user,
                                                  password=self.password)
        self.connection.autocommit = True

    def get_groups(self) -> list:
        """
        Get list of groups from DB
        :return: list
        """
        db_group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                db_group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return db_group_list

    def tear_down(self):
        """
        Close connection
        """
        self.connection.close()
