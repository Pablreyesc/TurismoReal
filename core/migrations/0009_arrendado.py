# Generated by Django 4.1.1 on 2022-11-06 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rentar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrendado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarifa', models.CharField(max_length=50)),
                ('condicion', models.CharField(max_length=50)),
                ('checkout', models.DateField()),
                ('checkin', models.DateField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.costumer')),
                ('departamento_id_depto', models.ForeignKey(db_column='departamento_id_depto', on_delete=django.db.models.deletion.DO_NOTHING, to='core.departamento')),
            ],
        ),
    ]
