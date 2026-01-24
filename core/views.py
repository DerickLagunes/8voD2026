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

def ruben(request):
    return render(request, "core/ruben.html")
def alexandro(request):
    return render(request, 'core/alexandro.html')
def OscarMontesCV(request):
    return render(request,"core/OscarMontesCV.html")

def cvjona(request):
    return render(request, "core/cvjona.html")

def cisco(request):
    return render(request, "core/cisco.html")

def cv(request):
    return render(request, "core/cv.html")
