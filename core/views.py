from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def contacto(request):
    print("El usuario entro al contacto")
    return render(request, "core/contacto.html")

def onepage(request):
    return render(request, "core/onepage.html")

def derick(request):
    return render(request, "core/derick.html")

def franciscoArmando(request):
    return render(request, "core/franciscoarmando.html")