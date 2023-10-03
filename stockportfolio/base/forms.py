from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import StockAccount

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class StockSymbolForm(forms.Form):
    stock_symbol = forms.CharField(max_length=15)


class StockAccountForm(forms.ModelForm):
    class Meta:
        model = StockAccount
        fields = ['account_number', 'account_name']


