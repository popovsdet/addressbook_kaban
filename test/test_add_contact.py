from model.contact import Contact


def test_add_group(app):
    app.contact.create(Contact(fistname="fistname_1", lastname="lastname_1",
                               address="address_1", mobile="mobile_1", email="email_1"))
