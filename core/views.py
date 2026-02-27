from django.shortcuts import render
from .forms import ContactoForm
from core.models import Contacto
from django.http import JsonResponse

def index(request):
    return render(request, "core/index.html")

def contacto(request):
    print("El usuario entro al contacto")
    return render(request, "core/contacto.html")

def onepage(request):
    return render(request, "core/onepage.html")

def derick(request):
    return render(request, "core/derick.html")

def daniel(request):
    return render(request, "core/danielCV.html")

def contacto_view(request):
    todos=Contacto.objects.all()
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            """
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
           
            print(f"--- NUEVO MENSAJE ---")
            print(f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}")
            """
            form.save()  # Guarda el contacto en la base de datos
            #return render(request, 'core/formulario.html', {'form': form, 'success': True, 'contactos': todos})
            # En lugar de renderizar, devolvemos una respuesta JSON para AJAX
            return JsonResponse({
                'status': 'ok',
                'message': 'Registro exitoso',
            })
        else:
            # Si el formulario no es válido, devolvemos los errores en formato JSON
            return JsonResponse({
                'status': 'error',
                'message': 'Algo salio mal',
                'errors': form.errors,
            }, status=400)
    else:
        form = ContactoForm()
    return render(request, 'core/formulario.html', {'form': form, 'contactos': todos})