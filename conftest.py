import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    app = Application()
    request.addfinalizer(app.tear_down)
    return app
