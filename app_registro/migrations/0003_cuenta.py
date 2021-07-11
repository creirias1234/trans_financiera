# Generated by Django 3.2.4 on 2021-07-10 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0002_rename_fecha_clientes_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('1', 'Activa'), ('2', 'Inactiva')], default='1', max_length=1)),
                ('clientes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_registro.clientes')),
            ],
        ),
    ]