import MySQLdb
import json
import itertools


class Database(object):
	username = "admin"
	hostname = "159.203.64.72"
	password = "pu8REmap!$wu3H"

	def __init__(self, database):
		self.database = database

	def connect(self):
		self.db = MySQLdb.connect(self.hostname, self.username, self.password, self.database)
		self.cur = self.db.cursor()
		print "Successfully connected to database!"

	def viewSubscribers(self):
		for row in self.getSubscribers():
			print row

	def getSubscribers(self):
		self.cur.execute("SELECT * FROM Subscriber")
		# raw_subscribers =self. cur.fetchall()

		# subscribers = json.dumps(raw_subscribers)
		return self.dictfetchall()

	def dictfetchall(self):
		"""Returns all rows from a cursor as a list of dicts"""
		desc = self.cur.description
		return [dict(itertools.izip([col[0] for col in desc], row))
				for row in self.cur.fetchall()]