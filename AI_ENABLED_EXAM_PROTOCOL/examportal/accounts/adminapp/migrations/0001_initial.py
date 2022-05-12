# Generated by Django 4.0.3 on 2022-04-27 17:04

import adminapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuser',
            fields=[
                ('fid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to=adminapp.models.filepath)),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=30)),
                ('phno', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'adminapp_fuser',
            },
        ),
        migrations.CreateModel(
            name='Suser',
            fields=[
                ('rollno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to=adminapp.models.filepath)),
                ('specification', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=10)),
                ('phno', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'adminapp_Suser',
            },
        ),
    ]