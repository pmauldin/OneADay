from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Interest(models.Model):
	keyword = models.CharField(db_column='Keyword', primary_key=True, max_length=30)
	link = models.CharField(db_column='Link', max_length=1000, blank=True, null=True)
	last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)

	def __str__(self):
		return self.keyword

	class Meta:
		db_table = 'Interest'

class Subscriber(models.Model):
	subscriberid = models.AutoField(db_column='SubscriberID', primary_key=True)
	user = models.ForeignKey(User, null=False)
	joindate = models.DateTimeField(db_column='JoinDate')
	keywords = models.ManyToManyField(Interest)

	def __str__(self):
		return self.user.username

	class Meta:
		db_table = 'Subscriber'
