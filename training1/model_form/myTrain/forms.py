from django import forms
from django.contrib.auth.models import User
from myTrain.models import Website

class UserInfoForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():

        model = User
        fields = ("username","email","password")

class UserWebsiteForm(forms.ModelForm):

    class Meta():

        model = Website
        fields = ('portfolio',)