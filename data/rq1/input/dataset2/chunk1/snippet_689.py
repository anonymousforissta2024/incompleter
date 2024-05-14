#Source: https://stackoverflow.com/questions/43274942/falcon-attributeerror-api-object-has-no-attribute-create
from falcon import testing
import pytest
from app import api


@pytest.fixture(scope='module')
def client():
    # Assume the hypothetical `myapp` package has a
    # function called `create()` to initialize and
    # return a `falcon.API` instance.
    return testing.TestClient(api.create())


def test_get_message(client):
    result = client.simulate_get('/')
    assert result.status_code == 200