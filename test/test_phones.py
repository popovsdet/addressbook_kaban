import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.all_phones_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    """
    # TODO: Check how it works
    1. Remove None phone numbers using filter().
    2. Clear each phone from "() -" using clear().
    3. Remove empty stings using filter().
    4. Create a new sting using join().
    :param contact: contact object
    :return: str
    """
    remove_none_phones = filter(lambda x: x is not None, [contact.home_phone, contact.work_phone, contact.mobile_phone,
                                                          contact.secondary_phone])
    clear_phones = map(lambda x: clear(x), remove_none_phones)
    remove_empty_phones = filter(lambda x: x != "", clear_phones)
    return "\n".join(remove_empty_phones)
