# Generated by Django 4.2 on 2023-07-03 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0006_alter_ficha_fecha_creación_alter_ficha_monto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='fecha_creación',
        ),
        migrations.AddField(
            model_name='ficha',
            name='fecha_creacion',
            field=models.DateField(default='2023-07-03'),
        ),
    ]
