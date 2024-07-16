# Generated by Django 5.0.4 on 2024-07-16 01:43

import django_cryptography.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0020_databaseconnection_extras_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseconnection',
            name='password',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='databaseconnection',
            name='user',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=255, null=True)),
        ),
    ]
