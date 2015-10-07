# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('keyword', models.CharField(max_length=30, serialize=False, primary_key=True, db_column='Keyword')),
                ('link', models.CharField(max_length=1000, null=True, db_column='Link', blank=True)),
                ('last_updated', models.DateTimeField(null=True, db_column='Last_Updated', blank=True)),
            ],
            options={
                'db_table': 'Interest',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('subscriberid', models.AutoField(serialize=False, primary_key=True, db_column='SubscriberID')),
                ('firstname', models.CharField(max_length=30, db_column='FirstName')),
                ('lastname', models.CharField(max_length=20, db_column='LastName')),
                ('email', models.CharField(unique=True, max_length=255, db_column='Email')),
                ('joindate', models.DateTimeField(db_column='JoinDate')),
                ('password', models.CharField(max_length=255, db_column='Password')),
                ('salt', models.CharField(max_length=120, db_column='Salt')),
            ],
            options={
                'db_table': 'Subscriber',
            },
        ),
        migrations.CreateModel(
            name='SubscriberInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscriberid', models.IntegerField(db_column='SubscriberID')),
                ('keyword', models.CharField(max_length=30, db_column='Keyword')),
            ],
            options={
                'db_table': 'SubscriberInterest',
            },
        ),
    ]
