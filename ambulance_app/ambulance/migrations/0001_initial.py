# Generated by Django 5.1.3 on 2024-11-08 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=20)),
                ('current_location', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('available', 'Available'), ('busy', 'Busy')], max_length=20)),
                ('driver_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=100)),
                ('requester_location', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ambulance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ambulance.ambulance')),
            ],
        ),
    ]
