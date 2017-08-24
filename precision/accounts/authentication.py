from precision.accounts.models import SchoolAdministrator # absolute import to be fixed

class EmailAuthBackend(object):
    """Authenticate using email account"""

    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

