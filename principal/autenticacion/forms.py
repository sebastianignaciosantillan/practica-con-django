from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Correo electrónico'}),
            'password1': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirmar contraseña'}),
        }
