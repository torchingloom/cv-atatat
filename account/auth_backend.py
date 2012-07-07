from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from registration.backends.default import DefaultBackend
from account.forms import RegistrationForm

class AuthBackend(DefaultBackend, ModelBackend):
    def get_form_class(self, request):
        return RegistrationForm

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(Q(email=username) | Q(username=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
