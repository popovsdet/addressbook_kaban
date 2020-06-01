"""
Test data for contacts.
"""
import random
import string

from model.contact import Contact


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(max_len))])


random_data = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", work_phone="",
                       secondary_phone="", email="")] + \
              [Contact(first_name=random_sting("first_name", 5), last_name=random_sting("last_name", 5),
                       address=random_sting("address", 5), home_phone=random_sting("h_p", 5),
                       mobile_phone=random_sting("m_p", 5), work_phone=random_sting("w_p", 5),
                       secondary_phone=random_sting("s_p", 10), email=random_sting("email", 5))
               for x in range(5)]

constant_data = [Contact(first_name="first_name_1", last_name="last_name_1", address="address_1",
                         home_phone="home_phone_1", mobile_phone="mobile_phone_1", work_phone="work_phone_1",
                         secondary_phone="secondary_phone_1", email="email_1"),
                 Contact(first_name="first_name_2", last_name="last_name_2", address="address_2",
                         home_phone="home_phone_2", mobile_phone="mobile_phone_2", work_phone="work_phone_2",
                         secondary_phone="secondary_phone_2", email="email_2")]
