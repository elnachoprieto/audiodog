# Generated by Django 2.2.7 on 2019-11-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiodog', '0010_auto_20191129_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
