#Source: https://stackoverflow.com/questions/58882030/how-do-i-fix-this-attributeerror-subrequest-object-has-no-attribute-getfunca
@pytest.fixture(autouse=True)
def _configure_application(request, monkeypatch):
    """Use `pytest.mark.options` decorator to pass options to your application
    factory::

        @pytest.mark.options(debug=False)
        def test_something(app):
            assert not app.debug, 'the application works not in debug mode!'

    """
    if 'app' not in request.fixturenames:
        return