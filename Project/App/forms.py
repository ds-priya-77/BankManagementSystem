from django.forms import ModelForm,NumberInput,TextInput,Select,DateInput
from .models import *

# Create your tests here.
class BankForm(ModelForm):
  class Meta:
    model=Bank
    fields='__all__'
    



    widgets = {
            'account_number': NumberInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Enter Account Number'
            }),
            'name': TextInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Enter Account Holder Name'
            }),
            'age': NumberInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Enter Age'
            }),
            'gender': Select(attrs={
                'class': 'form-select mb-3'
            }),
            'dob': DateInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'YYYY-MM-DD', 
                'type': 'date'
            }),
            'balance': NumberInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Enter Account Balance'
            }),
        }


class TransForm(ModelForm):
  class Meta:
    model=Transaction
    fields='__all__'


  

