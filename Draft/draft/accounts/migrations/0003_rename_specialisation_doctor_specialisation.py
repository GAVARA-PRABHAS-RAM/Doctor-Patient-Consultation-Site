# Generated by Django 5.0.7 on 2024-09-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_specialisation_doctor_specialisation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='specialisation',
            new_name='Specialisation',
        ),
    ]
