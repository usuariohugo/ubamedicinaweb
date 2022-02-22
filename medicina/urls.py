from django.urls import path
from medicina import views

urlpatterns = [
   #url principal
   path('',views.home,name="home"),
   #url link-barra
   path('contactos/',views.contactos,name="contactos"),
   path('docentes/',views.docentes,name="docentes"),
   path('administracion/',views.administracion,name="administracion"),
   #url barra-facultad
   path('informacionsobrelafacultad/',views.informacionsobrelafacultad,name="informacionsobrelafacultad"),
   path('biblioteca/',views.biblioteca,name="biblioteca"),
   path('departamentos/',views.departamentos,name="departamentos"),
   path('museo/',views.museo,name="museo"),
   path('nuevosespacios/',views.nuevosespacios,name="nuevosespacios"),
   path('noticiassobrelafacultad/',views.noticiassobrelafacultad,name="noticiassobrelafacultad"),
   #url-admision
   path('estudiantes/',views.estudiantes,name="estudiantes"), 
   path('carreras/',views.carreras,name="carreras"),
   path('extension/',views.extension,name="extension"),
   path('extranjeros/',views.extranjeros,name="extranjeros"),
   path('ingresantes/',views.ingresantes,name="ingresantes"),
   path('noticiaestudiantes/',views.noticiaestudiantes,name="noticiaestudiantes"),
]