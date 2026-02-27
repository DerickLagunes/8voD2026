from django import forms
from django.core.exceptions import ValidationError
import re

class RegistroForm(forms.Form):
    nombre = forms.CharField(
        min_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre', 'pattern': '[a-zA-ZáéíúóÁÉÍÚÓ ]{10,}', 'title': 'Ingresa mínimo 10 letras, solo texto'} )
    )
    matricula = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu matrícula', 'pattern': "\d{5}[a-zA-Z]{2}\d{3}", 'title': '5 números, 2 letras y 3 números'} )
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo institucional', 'pattern': "[a-zA-Z0-9]+@utez\.edu\.mx", "title": "Debe ser un correo @utez.edu.mx"} )
    )
    telefono = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu teléfono', 'pattern': "\d{10}", "title": "Ingresa un número de 10 dígitos"} )
    )
    rfc = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu RFC', 'pattern': "[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}", "title": "Ingresa tu RFC de 13 caracteres"} )
    )
    contrasenia = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu contraseña', 'pattern': "(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!#$%&?]).{8,}", "title": "Mínimo 8 caracteres, mayúscula, minúscula, número y símbolo"} )
    )
    
    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not re.match("^[a-zA-ZáéíúóÁÉÍÚÓ ]{10,}$", data):
            raise ValidationError("El nombre solo debe contener letras y espacios (mínimo 10 caracteres).")
        return data

    def clean_matricula(self):
        data = self.cleaned_data['matricula']
        if not re.match("^\d{5}[a-zA-Z]{2}\d{3}$", data):
            raise ValidationError("La matrícula debe tener 5 números, 2 letras y 3 números.")
        return data

    def clean_correo(self):
        data = self.cleaned_data['correo']
        if not re.match("^[a-zA-Z0-9]+@utez\.edu\.mx$", data):
            raise ValidationError("El correo debe ser institucional (@utez.edu.mx).")
        return data

    def clean_telefono(self):
        data = self.cleaned_data['telefono']
        if not re.match("^\d{10}$", data):
            raise ValidationError("El teléfono debe contener exactamente 10 dígitos.")
        return data

    def clean_rfc(self):
        data = self.cleaned_data['rfc']
        if not re.match("^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$", data):
            raise ValidationError("RFC inválido. Debe tener 13 caracteres y estar en mayúsculas.")
        return data

    def clean_contrasenia(self):
        data = self.cleaned_data['contrasenia']
        if not re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$", data):
            raise ValidationError(
                "La contraseña debe tener mínimo 8 caracteres, una mayúscula, una minúscula, un número y un símbolo especial."
            )
        return data
