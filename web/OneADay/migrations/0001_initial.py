# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('keyword', models.CharField(max_length=30, serialize=False, primary_key=True, db_column='keyword')),
                ('link', models.CharField(max_length=1000, null=True, db_column='link', blank=True)),
                ('last_updated', models.DateTimeField(null=True, db_column='last_updated', blank=True)),
            ],
            options={
                'db_table': 'Interest',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('subscriberid', models.AutoField(serialize=False, primary_key=True, db_column='SubscriberID')),
                ('joindate', models.DateTimeField(db_column='join_date')),
                ('last_emailed', models.DateTimeField(null=True, db_column='last_emailed', blank=True)),
                ('frequency', models.IntegerField(default=1, null=True, db_column='frequency')),
                ('keywords', models.ManyToManyField(to='OneADay.Interest')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Subscriber',
            },
        ),
    ]
