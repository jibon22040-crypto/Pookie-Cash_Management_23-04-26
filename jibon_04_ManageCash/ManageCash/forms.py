from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import UserModel, ProfileModel,AddCashModel,ExpenseModel

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email','password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['full_name', 'phone', 'address', 'profile_pic']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = ['source', 'amount', 'description']

        widgets ={
            'datetime': forms.DateTimeInput (attrs={'type':'date'})
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = ['description', 'amount']

        widgets ={
            'datetime': forms.DateTimeInput (attrs={'type':'date'})
        }