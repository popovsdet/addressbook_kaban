"""
Fixtures
"""
import pytest

from fixture.application import Application
from model.contact import Contact
from model.group import Group

app_fixture = None


@pytest.fixture(scope="function")
def app(request):
    """
    Before each test method:
     1. Create an application fixture
        - if it doesn't exist or
        - if fixture doesn't valid (no opened browser)
     2. Login
    :return: app fixture
    """
    global app_fixture
    if not app_fixture or not app_fixture.is_valid():
        # get option if we use hook pytest_addoption(parser) fist
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        app_fixture = Application(browser=browser, base_url=base_url)
    app_fixture.session.ensure_login(username="admin", password="secret")
    return app_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    """
    Close session.
    :param request: request
    """

    def fin():
        app_fixture.session.ensure_logout()
        app_fixture.tear_down()

    # Run after last test
    request.addfinalizer(fin)


@pytest.fixture(scope="function")
def add_first_group():
    """
    Create one group if no one exists
    """
    if not app_fixture.group.count():
        app_fixture.group.create(Group(name="test"))


@pytest.fixture(scope="function")
def add_first_contact():
    """
    Create one contact if no one exists
    """
    if not app_fixture.contact.count():
        app_fixture.contact.create(Contact(first_name="fist_name_1", last_name="last_name_2"))


# Hooks. Should be in conftest. Pytest check it automatically.
def pytest_addoption(parser):
    """
    Register command line options
    :param parser: parser for command line.
    In parser we use method addoption() with parameters: "--browser" and "--baseUrl" which add option.
    addoption() add parameter from command line. After that we can get if from request.config.getoption("--browser")
    action="store" means we save this parameter "--browser"
    """
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
