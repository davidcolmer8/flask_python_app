import pytest
from flaskPythonApp.app import create_app

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app
