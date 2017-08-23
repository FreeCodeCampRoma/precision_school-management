from django import forms
from precision.accounts.models import SchoolAdministrator # absolute import to be fixed


# CODE BELOW THIS LINE IS NOT USED, BUT PRESENT FOR EDUCATION PURPOSES
# ====================================================================
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
# ====================================================================


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = SchoolAdministrator
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match!')
        return cd['password2']


