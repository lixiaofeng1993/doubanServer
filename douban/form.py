# !/usr/bin/env python
# coding=utf-8
from django import forms
from douban.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['net_name', 'net_img', 'sex', 'age', 'phone', 'password']

    password2 = forms.CharField(max_length=128)

    def clean_password2(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('密码不一致')
