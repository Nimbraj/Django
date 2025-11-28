from django import forms
from django.core import validators


def email_validation(value):
    if not value.endswith('@gmail.com'):
        raise forms.ValidationError("Email must end with @gmail.com")


class Registration(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name'
    )

    email = forms.EmailField(
        label='Email',
        validators=[email_validation]
    )

    age = forms.IntegerField(
        label='Age'
    )

    marks = forms.CharField(
        label='Marks'
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=234,
        label='Password'
    )

    cpassword = forms.CharField(
        widget=forms.PasswordInput,
        max_length=234,
        label='Confirm Password'
    )

    feedback = forms.CharField(
        max_length=100,
        label='Feedback'
    )

    bot_data = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )

    # FIELD LEVEL VALIDATION
    def clean_name(self):
        data = self.cleaned_data.get("name")

        if len(data) < 4:
            raise forms.ValidationError(
                "Length of name should be greater than 4 characters"
            )

        return data

    # FORM LEVEL VALIDATION
    def clean(self):
        data = super().clean()

        age = data.get('age')
        password = data.get('password')
        cpassword = data.get('cpassword')
        bot = data.get('bot_data')

        if age is not None and age < 18:
            raise forms.ValidationError("Age should be greater than 18")

        if password and cpassword and password != cpassword:
            raise forms.ValidationError("Re-entered password does not match")

        if bot and len(bot) > 0:
            raise forms.ValidationError("Form submitted by bot — rejected")

        return data
