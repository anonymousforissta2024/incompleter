#Source: https://stackoverflow.com/questions/59012381/pytest-flask-application-attributeerror-module-src-api-has-no-attribute-test
import pytest
from src import api


api.testing = True
client = api.test_client()


def test_route(client):
    response = api.get('/')
    assert response.status_code == 200