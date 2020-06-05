from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from .models import Order

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user doesn\'t exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def clean_email(self):
        username = self.cleaned_data.get('username')
        return username


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'description', 'price']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'},)
        }