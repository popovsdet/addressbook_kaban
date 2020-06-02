from random import randrange

from model.contact import Contact


def test_modify_contact(app, add_first_contact, data_contacts):
    contact = data_contacts
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
