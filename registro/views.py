from django.shortcuts import render
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            
            nombre = form.cleaned_data['nombre']
            matricula = form.cleaned_data['matricula']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            rfc = form.cleaned_data['rfc']
            contrasenia = form.cleaned_data['contrasenia']
           
            print(f"--- NUEVO MENSAJE ---")
            print(f"Nombre: {nombre}\nMatricula: {matricula}\nCorreo: {correo}")
            return render(request, 'registro/formulario.html', {'form': form, 'success': True})
    else:
        form = RegistroForm()
   
    return render(request, 'registro/formulario.html', {'form': form})

