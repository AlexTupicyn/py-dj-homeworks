# Generated by Django 5.0.6 on 2024-06-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
