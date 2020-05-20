import pytest

from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.tear_down)
    return app


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(fistname="fistname_1", lastname="lastname_1",
                               address="address_1", mobile="mobile_1", email="email_1"))
    app.logout()