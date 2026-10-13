from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# user signup form
      # email is mandatory
          # django user model
              # fields for the form
class RegistrationFormForUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
