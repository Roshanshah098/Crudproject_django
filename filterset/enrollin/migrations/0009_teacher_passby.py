# Generated by Django 5.0.7 on 2024-08-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollin', '0008_subject_subject_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='passby',
            field=models.CharField(default='section1', max_length=40),
        ),
    ]
