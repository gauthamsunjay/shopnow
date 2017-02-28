from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.Form):
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirm Password",
                              widget=forms.PasswordInput)

  def clean_username(self):
    username = self.cleaned_data.get("username")
    if User.objects.filter(username__icontains=username).exists():
      raise forms.ValidationError("Username is already taken.")

    return username

  def clean_password2(self):
    password = self.cleaned_data.get("password")
    password2 = self.cleaned_data.get("password2")
    if password != password2:
      raise forms.ValidationError("Passwords don't match.")
    return password

  def clean_email(self):
    email = self.cleaned_data.get("email")
    if User.objects.filter(email__icontains=email).exists():
      raise forms.ValidationError("Email is already registered.")
    return email
