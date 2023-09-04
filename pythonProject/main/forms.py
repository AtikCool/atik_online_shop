from django.contrib.auth.forms import AuthenticationForm
from .models import User
class UserLoginForm(AuthenticationForm):
    class Meta:
        pass