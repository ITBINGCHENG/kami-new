from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="", max_length=128) #label为表单标签名
    password = forms.CharField(label="", max_length=256, widget=forms.PasswordInput)