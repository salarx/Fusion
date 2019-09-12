# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-12 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('is_read', models.BooleanField(default=False)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upload_designation', to='globals.Designation')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='globals.ExtraInfo')),
            ],
            options={
                'db_table': 'File',
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField(auto_now_add=True)),
                ('forward_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('upload_file', models.FileField(blank=True, upload_to='')),
                ('is_read', models.BooleanField(default=False)),
                ('current_design', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.HoldsDesignation')),
                ('current_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
                ('file_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filetracking.File')),
                ('receive_design', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rec_design', to='globals.Designation')),
                ('receiver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Tracking',
            },
        ),
    ]