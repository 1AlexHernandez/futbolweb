# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cancelacion(models.Model):
    idcancelacion = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=45, blank=True, null=True)
    reservas_idreservas = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_idreservas')
    reservas_personas_idpersonas = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_personas_idpersonas')
    reservas_personas_tipopersona_idtipopersona = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_personas_tipopersona_idtipopersona')
    reservas_personas_tipodocumento_idtipodocumento = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_personas_tipodocumento_idtipodocumento')
    reservas_servicios_idservicios = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_servicios_idservicios')

    class Meta:
        managed = False
        db_table = 'cancelacion'
        unique_together = (('idcancelacion', 'reservas_idreservas', 'reservas_personas_idpersonas', 'reservas_personas_tipopersona_idtipopersona', 'reservas_personas_tipodocumento_idtipodocumento', 'reservas_servicios_idservicios'),)


class Cancha(models.Model):
    idcancha = models.AutoField(primary_key=True)
    ubicacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    tipocancha_idtipocancha = models.ForeignKey('Tipocancha', models.DO_NOTHING, db_column='tipocancha_idtipocancha')
    estado_idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_idestado')

    class Meta:
        managed = False
        db_table = 'cancha'
        unique_together = (('idcancha', 'tipocancha_idtipocancha', 'estado_idestado'),)


class Estado(models.Model):
    idestado = models.AutoField(primary_key=True)
    disponible = models.DateTimeField(blank=True, null=True)
    fueraservicio = models.DateTimeField(blank=True, null=True)
    reservada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Franjahorarios(models.Model):
    idfranjahorarios = models.AutoField(primary_key=True)
    horaentrada = models.IntegerField(blank=True, null=True)
    horasalida = models.IntegerField(blank=True, null=True)
    horario_idhorario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='horario_idhorario')

    class Meta:
        managed = False
        db_table = 'franjahorarios'
        unique_together = (('idfranjahorarios', 'horario_idhorario'),)


class Horario(models.Model):
    idhorario = models.AutoField(primary_key=True)
    horario = models.IntegerField(blank=True, null=True)
    asignacion = models.CharField(max_length=45, blank=True, null=True)
    horarioapertura = models.IntegerField(blank=True, null=True)
    horariocierre = models.IntegerField(blank=True, null=True)
    dias = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Personas(models.Model):
    idpersonas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    correo_electronico = models.CharField(db_column='correo electronico', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    edad = models.IntegerField(blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    tipopersona_idtipopersona = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='tipopersona_idtipopersona')
    tipodocumento_idtipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipodocumento_idtipodocumento')

    class Meta:
        managed = False
        db_table = 'personas'
        unique_together = (('idpersonas', 'tipopersona_idtipopersona', 'tipodocumento_idtipodocumento'),)

class Reservas(models.Model):
    idreservas = models.AutoField(primary_key=True)
    fechareserva = models.DateField(blank=True, null=True)
    fechasolicitud = models.DateField(blank=True, null=True)
    cantidadpersonas = models.IntegerField(blank=True, null=True)
    personas_idpersonas = models.ForeignKey(Personas, models.DO_NOTHING, db_column='personas_idpersonas')
    personas_tipopersona_idtipopersona = models.ForeignKey(Personas, models.DO_NOTHING, db_column='personas_tipopersona_idtipopersona')
    personas_tipodocumento_idtipodocumento = models.ForeignKey(Personas, models.DO_NOTHING, db_column='personas_tipodocumento_idtipodocumento')
    servicios_idservicios = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='servicios_idservicios')
    franjahorarios_idfranjahorarios = models.ForeignKey(Franjahorarios, models.DO_NOTHING, db_column='franjahorarios_idfranjahorarios')
    cancha_idcancha = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='cancha_idcancha')
    cancha_tipocancha_idtipocancha = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='cancha_tipocancha_idtipocancha')
    cancha_estado_idestado = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='cancha_estado_idestado')

    class Meta:
        managed = False
        db_table = 'reservas'
        unique_together = (('idreservas', 'personas_idpersonas', 'personas_tipopersona_idtipopersona', 'personas_tipodocumento_idtipodocumento', 'servicios_idservicios', 'franjahorarios_idfranjahorarios', 'cancha_idcancha', 'cancha_tipocancha_idtipocancha', 'cancha_estado_idestado'),)


class Servicios(models.Model):
    idservicios = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    img = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'


class Tipocancha(models.Model):
    idtipocancha = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    numjugadores = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipocancha'


class Tipodocumento(models.Model):
    idtipodocumento = models.AutoField(primary_key=True)
    tipodocumento = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tipopersona(models.Model):
    idtipopersona = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipopersona'
