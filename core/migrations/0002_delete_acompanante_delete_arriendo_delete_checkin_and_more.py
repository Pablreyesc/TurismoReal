# Generated by Django 4.1.1 on 2022-09-09 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acompanante',
        ),
        migrations.DeleteModel(
            name='Arriendo',
        ),
        migrations.DeleteModel(
            name='Checkin',
        ),
        migrations.DeleteModel(
            name='Chekout',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Conductor',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='DetalleMantencion',
        ),
        migrations.DeleteModel(
            name='DetalleViaje',
        ),
        migrations.DeleteModel(
            name='Estadia',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
        migrations.DeleteModel(
            name='Mantencion',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.DeleteModel(
            name='ServicioExtra',
        ),
        migrations.DeleteModel(
            name='TipoDePago',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
        migrations.DeleteModel(
            name='Transporte',
        ),
        migrations.DeleteModel(
            name='Ubicacion',
        ),
    ]
