from django import forms


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=100, required=True, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(required=True, label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Again', 'class': 'form-control'}))
    email = forms.EmailField(required=True, label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))