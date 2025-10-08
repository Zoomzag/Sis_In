from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.log_in, name='log_in'),
    path("index/", views.index, name='index'),
    path("Modulo_1/", views.Modulo_1, name='Modulo_1'),
    path('Modulo_2/', views.Modulo_2, name='Modulo_2'),
    path('Modulo_3/', views.Modulo_3, name='Modulo_3'),
    path('Modulo_4/', views.Modulo_4, name='Modulo_4'),
    path('Modulo_5/', views.Modulo_5, name='Modulo_5'),
    path('Modulo_6/', views.Modulo_6, name='Modulo_6'),
    path('Modulo_7/', views.Modulo_7, name='Modulo_7'),
    
#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------
    path("base/", views.base, name='base'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("gestion_planes/", views.gestion_planes, name='gestion_planes'),
    path('control_horarios/', views.control_horarios, name='control_horarios'),
    path('evaluaciones/', views.evaluaciones, name='evaluaciones'),
    path('control_asistencia/', views.control_asistencia, name='control_asistencia'),
#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------


]
