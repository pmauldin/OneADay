# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneADay', '0003_auto_20151007_0010'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubscriberInterest',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='keywords',
            field=models.ManyToManyField(to='OneADay.Interest'),
        ),
    ]
