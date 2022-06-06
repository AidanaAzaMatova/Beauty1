
from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.db.models import fields
 
from .models import *

class RegistrForm(UserCreationForm):

  email = forms.EmailField(max_length=254, help_text='This field is required')
  

  class Meta:

    model = User
    fields = ('username', 'email', 'password1', 'password2', )

class CompForm(forms.ModelForm):
  
  class Meta:
    model=Company
    fields=('company_name','company_about','comapny_category','company_email','company_phone','company_logo',)
