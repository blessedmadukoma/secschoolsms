from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Principal, Staff
from django.db import transaction


class UserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(max_length=30)

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
  
  @transaction.atomic
  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']

    if commit:
      user.save()
    return user

class PrincipalUserForm(forms.ModelForm):
  class Meta:
    model = Principal
    fields = ('phone', 'schoolName')
    labels = {
      'phone': 'Phone Number',
      'schoolName': 'Name of Secondary School',
    }

class StaffForm(forms.ModelForm):
  class Meta:
    model = Staff
    fields = ('role', 'subjectTeaching', 'principal')
    labels = {
      'role': 'Staff Role',
      'principal': 'Principal Name',
      'subjectTeaching': 'Subject Teaching(if any)',
    }

  def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
      user.save()
    return user
  
  def __init__(self, *args, **kwargs):
    super(StaffForm, self).__init__(*args, **kwargs)
    self.fields['subjectTeaching'].required=False
    self.fields['role'].empty_label = "Select Staff Role..."
    self.fields['principal'].empty_label = "Select Principal..."