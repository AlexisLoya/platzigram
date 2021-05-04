"""User forms """
#Django
from django import forms
#Model
from django.contrib.auth.models import User
from users.models import Profile
class SignupForm(forms.Form):
    """Signup form"""
    #username = forms.CharField(min_length=4, max_length=50)

    username = forms.CharField(min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'username', 'class': 'form-control'}))

    password = forms.CharField(max_length=70, widget=forms.PasswordInput(
        attrs={'placeholder': 'password', 'class': 'form-control'}))

    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(
        attrs={'placeholder': 'repeat password', 'class': 'form-control'}))

    first_name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'first name', 'class': 'form-control'}))

    last_name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'last name', 'class': 'form-control'}))

    email = forms.CharField(min_length=6, max_length=50, widget=forms.EmailInput(
                            attrs={'placeholder': 'email', 'class': 'form-control'}))

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exists()
        if query:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password_confirmation != password:
            raise forms.ValidationError('Passwords don\'t match')
        return data

    def save(self):
        """create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    """Profile form"""
    website = forms.URLField(max_length=200, required=True)

    biography = forms.CharField(max_length=500, required=False)

    phone_number = forms.CharField(max_length=20, required=False)

    picture = forms.ImageField()