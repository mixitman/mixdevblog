from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False, max_length="250")
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length="500")


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # lines below are set up as a validation example
        #
        # email_base, provider = email.split("@")
        # domain, extension = provider.split('.')
        # if not extension == "edu":
        #     raise forms.ValidationError("Please use a valid .edu email address.")
        return email
