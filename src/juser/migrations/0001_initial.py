# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 09:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import juser.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=80)),
                ('uuid', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('SU', 'SuperUser'), ('GA', 'GroupAdmin'), ('CU', 'CommonUser')], default='CU', max_length=2)),
                ('ssh_key_pwd', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=juser.models.upload_to)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('comment', models.CharField(blank=True, max_length=160, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='admingroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juser.UserGroup'),
        ),
        migrations.AddField(
            model_name='admingroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(to='juser.UserGroup'),
        ),
    ]
