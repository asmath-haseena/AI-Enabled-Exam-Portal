# Generated by Django 4.0.3 on 2022-05-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccode', models.CharField(max_length=100)),
                ('tname', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
