from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    contacts = db.get_contacts()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.tear_down()
