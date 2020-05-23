from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify(Contact(fistname="fistname_2", lastname="lastname_2",
                               address="address_2", mobile="mobile_2", email="email_2"))


def test_modify_contact_name(app):
    app.contact.modify(Contact(fistname="fistname_4"))
