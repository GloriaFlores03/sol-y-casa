# Generated by Django 4.1.2 on 2023-02-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_foto_alter_cliente_options_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='compra',
            field=models.BooleanField(default=True),
        ),
    ]
