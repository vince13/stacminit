from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Student, Talent


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "password1": forms.PasswordInput(attrs={
                "class": "form-control"
            }),

            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
            })

        }

        # Customizing labels
        labels = {
            'password1': 'Password',
            'password2': 'Repeat Password',
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            "placeholder": "Enter username",
            "class": "form-control"
        }),
        label='Username'  # Optional: Customize the label
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder": "Enter password",
            "class": "form-control"
        }),
        label='Password'  # Optional: Customize the label
    )


# Form to register students
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['institution', 'state_of_residence',  'profile_image']

        widgets = {
            "institution": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "state_of_residence": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "profile_image": forms.FileInput(attrs={
                "class": "form-control"
            }),

        }


