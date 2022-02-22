from django.shortcuts import render

# link barra principal
def home(request):
    return render(request,'pages/home.html')

def contactos(request):
    return render(request,'pages/contactos.html')

def docentes(request):
    return render(request,'pages/docentes.html')

def administracion(request):
    return render(request,'pages/administracion.html')


#link sub-barra admision

def estudiantes(request):
    return render(request,'pages/admision/estudiantes.html')

def carreras(request):
    return render(request,'pages/admision/carreras.html')

def extension(request):
    return render(request,'pages/admision/extension.html')

def extranjeros(request):
    return render(request,'pages/admision/extranjeros.html')

def ingresantes(request):
    return render(request,'pages/admision/ingresantes.html')

def noticiaestudiantes(request):
    return render(request,'pages/admision/noticiaestudiantes.html')



#link sub-barra facultad

def informacionsobrelafacultad(request):
    return render(request,'pages/facultad/facultad.html')

def biblioteca(request):
    return render(request,'pages/facultad/biblioteca.html')

def departamentos(request):
    return render(request,'pages/facultad/departamentos.html')

def museo(request):
    return render(request,'pages/facultad/museo.html')

def noticiassobrelafacultad(request):
    return render(request,'pages/facultad/noticiasfacultad.html')

def nuevosespacios(request):
    return render(request,'pages/facultad/cecim.html')
