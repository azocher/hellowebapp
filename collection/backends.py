from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        # name of url we want to redirect to after successful registration_register
        return ('registration_create_thing')
