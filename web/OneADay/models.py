from __future__ import unicode_literals

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
	firstname = models.CharField(db_column='FirstName', max_length=30)
	lastname = models.CharField(db_column='LastName', max_length=30)
	email = models.CharField(db_column='Email', unique=True, max_length=255)
	joindate = models.DateTimeField(db_column='JoinDate')
	keywords = models.ManyToManyField(Interest)

	def __str__(self):
		return self.firstname + " " + self.lastname

	class Meta:
		db_table = 'Subscriber'
