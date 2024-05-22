from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class meta:
        model = Account
        fields = ["username","email","password"]