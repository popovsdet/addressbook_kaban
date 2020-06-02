"""
Fixtures
"""
import importlib
import json
import os

import jsonpickle
import pytest

from fixture.application import Application
from fixture.db import DbFixture
from model.contact import Contact
from model.group import Group

app_fixture = None
target = None


def load_config(file):
    global target
    if not target:
        path_to_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(path_to_file) as target_file:
            target = json.load(target_file)
    return target


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
    target_file_from_option = request.config.getoption("--target")
    web_config = load_config(target_file_from_option)["web"]
    if not target:
        # __file__ is current file. conftest.py
        # 1. Get absolute path to current directory using os.path.abspath(__file__)
        # 2. Get name of this directory using directory_name = os.path.dirname(os.path.abspath(__file__)
        # 3. Add a path to the file from option to this directory name using os.path.join(directory_name, target_file_from_option)
        path_to_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), target_file_from_option)
        # open target.json file
        with open(path_to_file) as target_file:
            # read data from target.json file
            target = json.load(target_file)
    if not app_fixture or not app_fixture.is_valid():
        # get option if we use hook pytest_addoption(parser) fist
        browser = request.config.getoption("--browser")
        app_fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    app_fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return app_fixture


@pytest.fixture(scope="session")
def db(request):
    target_file_from_option = request.config.getoption("--target")
    db_config = load_config(target_file_from_option)["db"]
    db_fixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                           password=db_config["password"])

    def fin():
        db_fixture.tear_down()

    request.addfinalizer(fin)
    return db_fixture


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
    """
    Pytest runs this method automatically each time BEFORE FIXTURES and add parametrization to the fixtures
    1. From all fixtures get only fixtures which starts with "data_" and "json_".
    2. Add parameters to this fixture: (fixture, test_data, ids=[str(x) for x in test_data]):
        fixture: this fixture
        test_data: iterable which we use in test
        ids=[str(x) for x in test_data]: beautiful representation

    :param metafunc: give you all info about a test (test function)
    """
    # check all fixtures in a test (test function) and put their names in fixturenames()
    # imetafunc.fixturenames looks like ['stop', 'app', 'json_contacts', 'request']
    for fixture in metafunc.fixturenames:
        # if fixture name starts with "data_" ...
        if fixture.startswith("data_"):
            # we download data from module (file)
            test_data = load_from_module(fixture[5:])
            # and put it as a parameter to this fixture
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module: str) -> list:
    """
    Load data from particular python file (module) in directory "data"
    :param module: name of the file
    :return: list of objects
    """
    # return importlib.import_module(f"data.{module}").constant_test_data
    return importlib.import_module(f"data.{module}").test_data


def load_from_json(file: str) -> list:
    """
    Get data from particular json file in directory "data".
    1. Get absolute path to current directory using os.path.abspath(__file__)
    2. Get name of this directory using directory_name = os.path.dirname(os.path.abspath(__file__)
    3. Add a path to the file from option to this directory name using os.path.join(directory_name, f"data/{file}.json")
    4. Open and read the file.
    5. Using jsonpickle.decode(f.read()) decode the file from json to objects

    :param file: name of the file
    :return: list of objects
    """
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.json")) as f:
        return jsonpickle.decode(f.read())
