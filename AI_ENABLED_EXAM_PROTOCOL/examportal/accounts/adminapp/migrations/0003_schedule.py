# Generated by Django 4.0.3 on 2022-04-29 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('ccode', models.CharField(max_length=30)),
                ('tname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=30)),
                ('ddate', models.DateField()),
                ('screated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'adminapp_schedule',
            },
        ),
    ]
