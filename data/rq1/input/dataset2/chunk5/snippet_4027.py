#Source: https://stackoverflow.com/questions/58631764/attribute-error-when-testing-flask-with-pytest-fixture
{...}

@pytest.fixture(scope='session', autouse=True)
def app(request):
    app = create_app({
        'TESTING': True
    })
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope='function')
def client(app, request):
    return app.test_client()

@pytest.fixture(scope='function')
def get(client):
    return humanize_werkzeug_client(client.get)