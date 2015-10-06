from random import SystemRandom

from backports.pbkdf2 import pbkdf2_hmac, compare_digest
from flask.ext.login import UserMixin

from db import database

class LoginUser(UserMixin):
	_password = None
	_salt = None

	def __init__(self, db):
		self.db = db

	def password(self):
		return self._password

	def is_valid_password(self, password):
		new_hash = self._hash_password(password)
		return compare_digest(new_hash, self._password)

	def _hash_password(self, password):
		pwd = password.encode("utf-8")
		salt = bytes(self._salt)
		buff = pbkdf2_hmac("sha512", pwd, salt, iterations=100000)
		return bytes(buff)

	def create(self, email):
		sql = "SELECT FROM Subscriber WHERE Email='%s'" % email
		return self.db.execute(sql)
