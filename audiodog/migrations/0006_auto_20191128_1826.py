# Generated by Django 2.2.7 on 2019-11-28 18:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audiodog', '0005_auto_20191128_1825'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Canciones',
            new_name='Cancion',
        ),
        migrations.RenameModel(
            old_name='Ciudades',
            new_name='Ciudad',
        ),
        migrations.RenameModel(
            old_name='Paises',
            new_name='Pais',
        ),
        migrations.RenameModel(
            old_name='Regiones',
            new_name='Region',
        ),
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]
