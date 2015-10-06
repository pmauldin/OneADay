from random import SystemRandom

from backports.pbkdf2 import pbkdf2_hmac, compare_digest
from flask.ext.login import UserMixin

from db import database

class User(UserMixin):
	_password = None
	_salt = None
	def __init__(self, db):
		self.db = db

	def _hash_password(self, password):
		pwd = password.encode("utf-8")
		salt = bytes(self._salt)
		buff = pbkdf2_hmac("sha512", pwd, salt, iterations=100000)
		return bytes(buff)

	def create(self, first_name, last_name, email, password):
		self._salt = bytes(SystemRandom().getrandbits(128))
		self._password = self._hash_password(password)