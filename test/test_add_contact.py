from model.contact import Contact


def test_add_group(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(first_name="fistname_1", last_name="lastname_1",
                      address="address_1", mobile_phone="mobile_1", email="email_1")
    app.contact.create(contact)
    new_contacts_count = app.contact.count()
    assert len(old_contact_list) + 1 == new_contacts_count, \
        f"Old list '{old_contact_list}' != new list '{new_contacts_count}'"
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max), \
        f"Old list '{old_contact_list}' != new list '{new_contact_list}'"
