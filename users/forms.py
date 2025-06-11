import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _

# UserCreationForm
class CustomUserCreationForm (UserCreationForm):
    class meta (UserCreationForm.meta):
        model = User
        # The password 1 and 2 are for the interface.
        # only receives one field as password, the
        # UserCreationForm does all the work.
        fields = ['email', 'password1', 'password2']

    # Builder
    def __init__(self, *args, **kwargs):
            # Takes care of all the initial configuration: 
            # creates the fields, sets up validations, etc.
            super().__init__(*args, **kwargs)
            
            # To translate the text
            self.fields['email'].label = _('Correo Electrónico')
            
            # Validate that the password is not common, etc.
            self.fields['password1'].help_text = password_validation.password_validators_help_text_html()