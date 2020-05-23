import pytest

from fixture.application import Application
from model.group import Group

fixture = None


@pytest.fixture(scope="function")
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.tear_down()

    request.addfinalizer(fin)


@pytest.fixture(scope="function")
def check_group():
    if not fixture.group.number():
        fixture.group.create(Group(name="test"))
