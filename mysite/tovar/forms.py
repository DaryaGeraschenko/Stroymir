from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text")
    rating = forms.IntegerField(label="Rating", max_value=5, min_value=1)


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RegistrationForm(LoginForm):
    email = forms.EmailField(label="Email")