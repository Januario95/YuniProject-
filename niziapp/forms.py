from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'style': 'width: 200px;'
                               }))
    email = forms.CharField(max_length=30,
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'style': 'width: 200px;'
                            }))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'style': 'width: 200px;'
                               }))

    password2 = forms.CharField(max_length=30,
                                label='Confirm password',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'style': 'width: 200px;'
                                }))

    class Meta:
        model = User
        fields = ['username', 'email',
                  'password', 'password2']

    # def clean_password(self):
    #     data = self.cleaned_data
    #     if data['password'] != self.password2:
    #         raise forms.ValidationError('Password did not match')

    #     return self.password


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'style': 'width: 200px;'
                               }))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'style': 'width: 200px;'
                               }))

    # class Meta:
    #     model = User
    #     fields = ['username', 'password']
