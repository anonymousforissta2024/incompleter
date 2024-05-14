#Source: https://stackoverflow.com/questions/70885979/trying-to-test-flask-endpoint-attributeerror-posixpath-object-has-no-attribu
# conftest.py

# ... imports here ...

@pytest.fixture
def client():
    app.config.from_object(TestSettings)
    with app.test_client() as client:
        with app.app_context():
            # starts connection with tests db
            db = MongoEngine(app)

        yield client  # Do the tests

        with app.app_context():
            # drop db after tests
            db.connection.drop_database('test')