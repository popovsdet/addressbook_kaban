import random
from random import randrange
import string

import pytest

from model.contact import Contact


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(max_len))])


test_data = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", work_phone="",
                     secondary_phone="", email="")] + \
            [Contact(first_name=random_sting("first_name", 5), last_name=random_sting("last_name", 5),
                     address=random_sting("address", 5), home_phone=random_sting("h_p", 5),
                     mobile_phone=random_sting("m_p", 5), work_phone=random_sting("w_p", 5),
                     secondary_phone=random_sting("s_p", 10), email=random_sting("email", 5))
             for x in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_modify_contact(app, add_first_contact, contact):
    old_contact_list = app.contact.get_contact_list()

    index = randrange(len(old_contact_list))
    contact.id = old_contact_list[index].id
    app.contact.modify(contact=contact, index=index)
    new_contact_list = app.contact.get_contact_list()

    assert len(old_contact_list) == len(new_contact_list), \
        f"Old list '{old_contact_list}' != new list '{new_contact_list}'"

    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max), \
        f"Old list '{old_contact_list}' != new list '{new_contact_list}'"
