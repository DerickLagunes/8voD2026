from django import forms
from django.core.exceptions import ValidationError

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        min_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre',
         'pattern': '^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{10,}$',
            'title': 'solo letras y espacios'})
        
    )

    matriculaUtez=forms.CharField(
min_length=10,
widget=forms.TextInput(attrs={'class': 'form-control', 'placelhoder': 'ingresa tu matricula',
       'pattern': '^\d{5}[A-Za-z]{2}\d{3}$',
       'title': 'Formato específico: 5 dígitos, 2 letras, 3 dígitos'})

    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    # Validación de Backend
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if "spam" in data.lower():
            raise ValidationError("No se permite contenido publicitario.")
        return data