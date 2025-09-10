from django.db import models

#Para la creacion de estos modelos se uso la funcion de django python manage.py inspectdb, si tienes dudas 
#consultar la documentacion de django: https://docs.djangoproject.com/en/5.2/

#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------

class Alertas(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey('Alumnos', models.DO_NOTHING, db_column='id_alumno', blank=True, null=True)
    tipo = models.CharField(max_length=17, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    leida = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alertas'


class Alumnos(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_grupo = models.ForeignKey('Grupos', models.DO_NOTHING, db_column='id_grupo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumnos'


class Asignaturas(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    id_carrera = models.ForeignKey('Carreras', models.DO_NOTHING, db_column='id_carrera', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    creditos = models.IntegerField(blank=True, null=True)
    horas_semana = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignaturas'


class Asistencias(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='id_alumno', blank=True, null=True)
    id_horario = models.ForeignKey('Horarios', models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    presente = models.IntegerField(blank=True, null=True)
    justificante = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencias'


class Calificaciones(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumnos, models.DO_NOTHING, db_column='id_alumno', blank=True, null=True)
    id_asignatura = models.ForeignKey(Asignaturas, models.DO_NOTHING, db_column='id_asignatura', blank=True, null=True)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    periodo = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Carreras(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    perfil_egreso = models.TextField(blank=True, null=True)
    plan_estudios_documento = models.TextField(blank=True, null=True)
    mapa_curricular = models.TextField(blank=True, null=True)
    vigente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras'


class Docentes(models.Model):
    id_docente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    disponibilidad = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docentes'


class Grupos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    id_carrera = models.ForeignKey(Carreras, models.DO_NOTHING, db_column='id_carrera', blank=True, null=True)
    nombre_grupo = models.CharField(max_length=50, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos'


class Horarios(models.Model):
    id_horario = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='id_grupo', blank=True, null=True)
    id_asignatura = models.ForeignKey(Asignaturas, models.DO_NOTHING, db_column='id_asignatura', blank=True, null=True)
    id_docente = models.ForeignKey(Docentes, models.DO_NOTHING, db_column='id_docente', blank=True, null=True)
    dia_semana = models.CharField(max_length=9, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horarios'
#------------------ZONA DE "Administracion_academica"-----------------------------------------------------------------------
