"""
Fixtures
"""
import importlib
import json
import os

import pytest

from fixture.application import Application
from model.contact import Contact
from model.group import Group

app_fixture = None
target = None


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
    global target
    if not target:
        path_to_file_from_option = request.config.getoption("--target")
        # __file__ is current file. conftest.py
        # 1. Get absolute path to current directory using os.path.abspath(__file__)
        # 2. Get name of this directory using directory_name = os.path.dirname(os.path.abspath(__file__)
        # 3. Add a path to the file from option to this directory name using os.path.join(directory_name, path_to_file_from_option)
        path_to_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), path_to_file_from_option)
        # get data from target.json file ones
        with open(path_to_file) as config_file:
            target = json.load(config_file)
    if not app_fixture or not app_fixture.is_valid():
        # get option if we use hook pytest_addoption(parser) fist
        browser = request.config.getoption("--browser")
        app_fixture = Application(browser=browser, base_url=target["baseUrl"])
    app_fixture.session.ensure_login(username=target["username"], password=target["password"])
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
    In parser we use method addoption() with parameters: "--browser"  which add option.
    addoption() add parameter from command line. After that we can get if from request.config.getoption("--browser")
    action="store" means we save this parameter "--browser"
    """
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        # Get file which starts with "data_"
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])



def load_from_module(module):
    return importlib.import_module(f"data.{module}").constant_test_data

def load_from_json(file):
    pass