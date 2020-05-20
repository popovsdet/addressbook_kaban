import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.tear_down)
    return app


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
