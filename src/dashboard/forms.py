from django.contrib.auth.models import User

from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']

class CredentialForm(forms.Form):
    aws_access_key = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'size': '30'}))
    aws_secret_access_key = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'size': '30'}))
    aws_session_token = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'size': '30'}))
    IamFleetRole = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'size': '30'}))
    TargetCapacity = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Number of Instances'}))
    imageId = forms.CharField(max_length=300,required=True,widget=forms.TextInput(attrs={'size': '40','placeholder': 'imageId'}))
    InstanceType = forms.CharField(max_length=300,required=True,widget=forms.TextInput(attrs={'size': '40','placeholder': 'InstanceType'}))
    SubnetId = forms.CharField(max_length=300,required=True,widget=forms.TextInput(attrs={'size': '40','placeholder': 'SubnetId'}))
    spotPrice = forms.DecimalField(decimal_places=2,required=True)
    time_of_expiration = forms.DateTimeField(required=True,widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd hh:mm:ss'}))

