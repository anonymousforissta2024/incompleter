#Source: https://stackoverflow.com/questions/59348642/django-registration-type-error-at-accounts-register-get-success-url-missing
from registration.backends.simple.views import RegistrationView


# my new reg view, subclassing RegistrationView from our plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        # the named URL that we want to redirect to after
        # successful registration
        return ('registration_create_word')