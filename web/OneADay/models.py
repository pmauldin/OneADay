from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Interest(models.Model):
	keyword = models.CharField(db_column='keyword', primary_key=True, max_length=30)
	link = models.CharField(db_column='link', max_length=1000, blank=True, null=True)
	last_updated = models.DateTimeField(db_column='last_updated', blank=True, null=True)

	def __str__(self):
		return self.keyword

	class Meta:
		db_table = 'Interest'


class Subscriber(models.Model):
	subscriberid = models.AutoField(db_column='SubscriberID', primary_key=True)
	user = models.ForeignKey(User, null=False)
	joindate = models.DateTimeField(db_column='join_date')
	last_emailed = models.DateTimeField(db_column='last_emailed', blank=True, null=True)
	frequency = models.IntegerField(db_column="frequency", null=True, default=1)
	keywords = models.ManyToManyField(Interest)

	def __str__(self):
		return self.user.username

	class Meta:
		db_table = 'Subscriber'
