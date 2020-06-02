"""
Tests for add contacts.
Use data from "data" directory. random_data or constant_data
"""

from model.contact import Contact


def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts_count = app.contact.count()
    assert len(old_contact_list) + 1 == new_contacts_count, \
        f"Old list '{old_contact_list}' != new list '{new_contacts_count}'"
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max), \
        f"Old list '{old_contact_list}' != new list '{new_contact_list}'"
