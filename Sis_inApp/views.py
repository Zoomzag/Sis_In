from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Carreras, Grupos, Alumnos, Docentes, Asignaturas, Horarios, Calificaciones, Asistencias, Alertas
from django.db.models import Count, Avg, Q
from django.utils import timezone

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'log_in.html', {'form': {'errors': True}})
    return render(request, 'log_in.html')

def index(request):
    return render(request,'index.html', {})

def Modulo_1(request):
    return render(request, 'Modulo_1/base.html')

def Modulo_2(request):
    return render(request, 'Modulo_2/index.html')

def Modulo_3(request):
    return render(request, 'Modulo_3/index.html')

def Modulo_4(request):
    return render(request, 'Modulo_4/index.html')

def Modulo_5(request):
    return render(request, 'Modulo_5/index.html')

def Modulo_6(request):
    return render(request, 'Modulo_6/index.html')   

def Modulo_7(request):
    return render(request, 'Modulo_7/index.html')   

#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------

def base(request):
    return render(request, 'Administracion_academica/base.html')

def dashboard(request):
   
    planes_count = Carreras.objects.count()
    estudiantes_count = Alumnos.objects.count()
    docentes_count = Docentes.objects.count()
    grupos_count = Grupos.objects.count()

    alertas_recientes = Alertas.objects.filter(leida=False).order_by('-fecha')[:5]
    
    actividades = [
        {'fecha': timezone.now().date(), 'descripcion': 'Sistema de administración académica iniciado'},
        {'fecha': timezone.now().date(), 'descripcion': f'{estudiantes_count} estudiantes registrados'},
        {'fecha': timezone.now().date(), 'descripcion': f'{docentes_count} docentes activos'},
    ]
    
    context = {
        'planes_count': planes_count,
        'estudiantes_count': estudiantes_count,
        'docentes_count': docentes_count,
        'grupos_count': grupos_count,
        'alertas': alertas_recientes,
        'actividades': actividades,
        'active_page': 'dashboard'
    }
    return render(request, 'Administracion_academica/dashboard.html', context)

def gestion_planes(request):
  
    planes = Carreras.objects.all()
    
    
    procesos = [
        {
            'entrada': 'Requisitos normativos',
            'salida': 'Plan de estudios', 
            'justificacion': 'Se genera un documento que contiene toda la información respecto a la carrera'
        },
        {
            'entrada': 'Perfil de egreso',
            'salida': 'Mapa curricular', 
            'justificacion': 'Se genera una representación visual del plan de estudios'
        },
        {
            'entrada': 'Propuesta académica',
            'salida': 'Catalogo de asignaturas', 
            'justificacion': 'Se genera una lista de todas las asignaturas disponibles, así como sus horarios'
        },
    ]
    
    context = {
        'procesos': procesos,
        'planes': planes,
        'active_page': 'gestion'
    }
    return render(request, 'Administracion_academica/gestion_planes.html', context)

def control_horarios(request):
   
    grupos = Grupos.objects.select_related('id_carrera').all()
    
  
    docentes = Docentes.objects.annotate(
        num_asignaturas=Count('horarios__id_asignatura', distinct=True)
    )
    
    horarios = Horarios.objects.select_related(
        'id_grupo', 'id_asignatura', 'id_docente'
    )[:10]  
    
    context = {
        'grupos': grupos,
        'docentes': docentes,
        'horarios': horarios,
        'active_page': 'control'
    }
    return render(request, 'Administracion_academica/control_horarios.html', context)

def evaluaciones(request):
    
    grupos = Grupos.objects.select_related('id_carrera').all()
    
  
    asignaturas = Asignaturas.objects.select_related('id_carrera').all()
   
    alertas_riesgo = Alertas.objects.filter(
        tipo='Baja calificación', 
        leida=False
    ).select_related('id_alumno')[:5]
 
    calificaciones_recientes = Calificaciones.objects.select_related(
        'id_alumno', 'id_asignatura'
    ).order_by('-id_calificacion')[:5]
    
    context = {
        'grupos': grupos,
        'asignaturas': asignaturas,
        'alertas_riesgo': alertas_riesgo,
        'calificaciones_recientes': calificaciones_recientes,
        'active_page': 'evaluaciones'
    }
    return render(request, 'Administracion_academica/evaluaciones.html', context)

def control_asistencia(request):
    
    grupos = Grupos.objects.select_related('id_carrera').all()
    

    asignaturas = Asignaturas.objects.select_related('id_carrera').all()

    alertas_inasistencia = Alertas.objects.filter(
        tipo='Inasistencias', 
        leida=False
    ).select_related('id_alumno')[:5]
    
 
    asistencias_recientes = Asistencias.objects.select_related(
        'id_alumno', 'id_horario'
    ).order_by('-fecha')[:5]
    
    
    total_asistencias = Asistencias.objects.count()
    total_presentes = Asistencias.objects.filter(presente=True).count()
    porcentaje_asistencia = (total_presentes / total_asistencias * 100) if total_asistencias > 0 else 0
    
    context = {
        'grupos': grupos,
        'asignaturas': asignaturas,
        'alertas_inasistencia': alertas_inasistencia,
        'asistencias_recientes': asistencias_recientes,
        'porcentaje_asistencia': round(porcentaje_asistencia, 2),
        'active_page': 'asistencia'
    }
    return render(request, 'Administracion_academica/control_asistencia.html', context)
#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------