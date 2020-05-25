from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    old_contact_list = app.contact.get_contacts()

    index = randrange(len(old_contact_list))
    contact_id = old_contact_list[index].id
    contact = Contact(first_name="fistname_2", last_name="lastname_2",
                      address="address_2", mobile="mobile_2", email="email_2", id=contact_id)
    app.contact.modify(contact, index)
    new_contact_list = app.contact.get_contacts()

    assert len(old_contact_list) == len(new_contact_list), \
        f"Old list '{old_contact_list}' != new list '{new_contact_list}'"

    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max), \
        f"Old list '{old_contact_list}' != new list '{new_contact_list}'"

# def test_modify_contact_name(app):
#     app.contact.modify(Contact(first_name="fistname_4"))
