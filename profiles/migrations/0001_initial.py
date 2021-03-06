# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default='0.00', help_text='amount of USD, for instance 10.55', max_digits=10, verbose_name='Balance')),
                ('pin_code', models.PositiveIntegerField(help_text='For instance XXXX where X is any number from 0 to 9', verbose_name='Pin code')),
                ('is_closed', models.BooleanField(default=False, help_text='Designates whether this profile should be treated as closed. ', verbose_name='is closed')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='accounts.Client', verbose_name='Client')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'verbose_name': 'Profile',
            },
        ),
    ]
