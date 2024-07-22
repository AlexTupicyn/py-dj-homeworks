# Generated by Django 5.0.6 on 2024-07-20 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
    ]
