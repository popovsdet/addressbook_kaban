from sys import maxsize


class Contact(object):
    def __init__(self, first_name=None, last_name=None, address=None, all_phones_home_page=None, home_phone=None,
                 mobile_phone=None, work_phone=None, secondary_phone=None, email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.all_phones_home_page = all_phones_home_page
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.id = id

    def __repr__(self):
        return f"id = '{self.id}': first_name = '{self.first_name}': last_name = '{self.last_name}': " \
               f"home_phone = '{self.home_phone}': mobile_phone = '{self.mobile_phone}'" \
               f": work_phone = '{self.work_phone}': secondary_phone = '{self.secondary_phone}'"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
