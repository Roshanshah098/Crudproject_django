# Generated by Django 5.0.7 on 2024-07-26 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollin', '0006_student_student_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Student_age',
            new_name='student_age',
        ),
    ]
