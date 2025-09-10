from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.log_in, name='log_in'),
    path("index/", views.index, name='index'),
#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------
    path("base/", views.base, name='base'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("gestion_planes/", views.gestion_planes, name='gestion_planes'),
    path('control_horarios/', views.control_horarios, name='control_horarios'),
    path('evaluaciones/', views.evaluaciones, name='evaluaciones'),
    path('control_asistencia/', views.control_asistencia, name='control_asistencia'),
#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------


]
