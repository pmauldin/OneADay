import MySQLdb
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

	def execute(self, sql):
		self.cur.execute(sql)
		return self.dictfetchall()

	def getSubscribers(self):
		return self.execute("SELECT * FROM Subscriber")

	def dictfetchall(self):
		"""Returns all rows from a cursor as a list of dicts"""
		desc = self.cur.description
		return [dict(itertools.izip([col[0] for col in desc], row))
				for row in self.cur.fetchall()]