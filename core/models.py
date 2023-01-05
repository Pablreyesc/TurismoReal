# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Acompanante(models.Model):
    id_acompanante = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut_acomp = models.CharField(primary_key=True, max_length=11)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    edad = models.BigIntegerField()
    sexo = models.CharField(max_length=30)
    cliente_rut_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_rut_cliente')

    class Meta:
        managed = False
        db_table = 'acompanante'


class Arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True)
    tarifa = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50)
    cliente_rut_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_rut_cliente')
    departamento_id_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_id_depto')
    checkout_id_checkout = models.ForeignKey('Checkout', models.DO_NOTHING, db_column='checkout_id_checkout')
    checkin_id_checkin = models.ForeignKey('Checkin', models.DO_NOTHING, db_column='checkin_id_checkin')

    class Meta:
        managed = False
        db_table = 'arriendo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Checkin(models.Model):
    id_checkin = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()

    class Meta:
        managed = False
        db_table = 'checkin'


class Checkout(models.Model):
    id_checkout = models.AutoField(primary_key=True)
    fecha_regreso = models.DateField()

    class Meta:
        managed = False
        db_table = 'checkout'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut_cliente = models.CharField( max_length=11)
    email = models.CharField(max_length=20)
    telefono = models.IntegerField()
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)
    usuario = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'cliente'


class Conductor(models.Model):
    id_conductor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conductor'


class Departamento(models.Model):
    id_depto = models.AutoField(primary_key=True)
    nombre_depto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    num_depto = models.IntegerField()
    muebles = models.CharField(max_length=50)
    internet = models.CharField(max_length=50)
    cable = models.CharField(max_length=50)
    calefaccion = models.CharField(max_length=50)
    precio = models.BigIntegerField()
    direccion = models.CharField(max_length=100)
    ubicacion_id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion_id_ubicacion')
    inventario_id_inventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='inventario_id_inventario')
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'departamento'

    def __str__(self):

        return self.nombre_depto


class DetalleMantencion(models.Model):
    id_detalle = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    mantencion_id_mantencion = models.ForeignKey('Mantencion', models.DO_NOTHING, db_column='mantencion_id_mantencion')
    departamento_id_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depto')

    class Meta:
        managed = False
        db_table = 'detalle_mantencion'


class DetalleViaje(models.Model):
    id_detalle = models.DecimalField(max_digits=11, decimal_places=11)
    descripcion = models.CharField(max_length=100)
    checkout_id_checkout = models.OneToOneField(Checkout, models.DO_NOTHING, db_column='checkout_id_checkout')
    checkin_id_checkin = models.OneToOneField(Checkin, models.DO_NOTHING, db_column='checkin_id_checkin')
    funcionario_rut_fun = models.OneToOneField('Funcionario', models.DO_NOTHING, db_column='funcionario_rut_fun')
    detalle_viaje_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'detalle_viaje'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Funcionario(models.Model):
    id_funcionario = models.IntegerField()
    nombre_fun = models.CharField(max_length=20)
    rut_fun = models.CharField(primary_key=True, max_length=50)
    apellido_fun = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=30)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'funcionario'


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    fecha_inventario = models.DateField()

    class Meta:
        managed = False
        db_table = 'inventario'
    
    def __str__(self):

        return self.descripcion


class Mantencion(models.Model):
    id_mantencion = models.IntegerField(primary_key=True)
    tipo_mant = models.CharField(max_length=50)
    fecha_mant = models.DateField()
    valor = models.BigIntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mantencion'


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField()
    comentario = models.CharField(max_length=100)
    valor = models.BigIntegerField()
    cant_acompanante = models.IntegerField(blank=True, null=True)
    departamento_id_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class ServicioExtra(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    reserva_id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='reserva_id_reserva')

    class Meta:
        managed = False
        db_table = 'servicio_extra'


class TipoDePago(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=11, decimal_places=11)
    credito = models.DecimalField(max_digits=15, decimal_places=15)
    debito = models.DecimalField(max_digits=15, decimal_places=15)
    arriendo_id_arriendo = models.ForeignKey(Arriendo, models.DO_NOTHING, db_column='arriendo_id_arriendo')

    class Meta:
        managed = False
        db_table = 'tipo_de_pago'


class Tour(models.Model):
    id_tour = models.IntegerField(primary_key=True)
    nombre_tour = models.CharField(max_length=50)
    valor = models.BigIntegerField()
    fecha_tour = models.DateField()
    hora_tour = models.CharField(max_length=50)
    arriendo_id_arriendo = models.ForeignKey(Arriendo, models.DO_NOTHING, db_column='arriendo_id_arriendo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class Transporte(models.Model):
    id_transporte = models.IntegerField(primary_key=True)
    nombre_transporte = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    conductor_id_conductor = models.OneToOneField(Conductor, models.DO_NOTHING, db_column='conductor_id_conductor')
    arriendo_id_arriendo = models.ForeignKey(Arriendo, models.DO_NOTHING, db_column='arriendo_id_arriendo')

    class Meta:
        managed = False
        db_table = 'transporte'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    cod_postal = models.BigIntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ubicacion'

    def __str__(self):

        return self.descripcion

class Costumer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):

        return self.nombre


class Order(models.Model):
    fecha_reserva = models.DateField()
    comentario = models.CharField(max_length=100)
    valor = models.BigIntegerField()
    cant_acompanante = models.IntegerField(blank=True, null=True)
    departamento_id_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depto', blank=True, null=True)
    customer = models.ForeignKey(Costumer, null=True, on_delete=models.SET_NULL)

class Rentar(models.Model):
    tarifa = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50)
    departamento_id_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_id_depto')
    checkout = models.DateField()
    checkin = models.DateField()

class Arrendado(models.Model):
    tarifa = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50)
    departamento_id_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_id_depto')
    checkout = models.DateField()
    checkin = models.DateField()
    customer = models.ForeignKey(Costumer, null=True, on_delete=models.SET_NULL)


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre

class OrdenDeCompra(models.Model):
    customer = models.ForeignKey(Costumer, null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, default=3)
    token_ws = models.CharField(max_length=255, default='0')
    tarjeta = models.CharField(max_length=10, default='0')
    fecha_transbank = models.CharField(max_length=100, default='0')
    estado_transbank = models.CharField(max_length=100, default='0')
    valor = models.PositiveBigIntegerField(default='0')

    def __str__(self) -> str:
        return f"N°{self.id}"

class OrdenDeCompra1(models.Model):
    customer = models.ForeignKey(Costumer, null=True, on_delete=models.SET_NULL)
    departamento_id_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_id_depto')
    estado = models.ForeignKey(Estado, models.DO_NOTHING, default=3)
    token_ws = models.CharField(max_length=255, default='0')
    tarjeta = models.CharField(max_length=10, default='0')
    fecha_transbank = models.CharField(max_length=100, default='0')
    estado_transbank = models.CharField(max_length=100, default='0')
    valor = models.PositiveBigIntegerField(default='0')

    def __str__(self) -> str:
        return f"N°{self.id}"


class ServicioExtra1(models.Model):
    descripcion = models.CharField(max_length=50)
    valor = models.BigIntegerField()
    reserva = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):

        return self.descripcion



