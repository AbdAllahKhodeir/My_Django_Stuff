from django import forms
from django.core.exceptions import ValidationError


class FormName(forms.Form):

    name = forms.CharField()

    email = forms.EmailField()

    verify_email = forms.EmailField(label='Enter your email again')

    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")

        vmail = cleaned_data.get("verify_email")

        if email != vmail:
            raise ValidationError("Emails are not the same")
