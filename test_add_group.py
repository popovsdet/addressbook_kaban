import pytest

from application import Application
from group import Group


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.tear_down)
    return app


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="name_1", header="header_1", footer="footer_1"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
