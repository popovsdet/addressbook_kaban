from random import randrange


def test_delete_first_contact(app, add_first_contact):
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete(index=index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list), \
        f"Len of old list '{old_contact_list}' != new list '{new_contact_list}'"
    del old_contact_list[index]
    assert old_contact_list == new_contact_list, f"Old list '{old_contact_list}' != new list '{new_contact_list}'"
