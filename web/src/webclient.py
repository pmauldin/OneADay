from db.database import Database
# from auth.login import LoginUser

from flask import (
	Flask,
	redirect,
	render_template,
	request,
	url_for,
)

app = Flask(__name__)
username = "admin"
hostname = "159.203.64.72"
password = "pu8REmap!$wu3H"
SECRET_KEY = 'flask-session-insecure-secret-key'
SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'

# db = None
#
# @app.route("/login")
# def login():
# 	# if request.method == 'GET':
# 		# print request.args
# 	if db is None:
#
# 	user = LoginUser(db)
# 	subscribers = user.create('petermauldin1@gmail.com')
# 	return render_template(
# 		'subscribers_interests.html',
# 		subscribers=subscribers)
#
#	return render_template('login.html')

@app.route("/signup, methods=['GET', 'POST']")
def signup():
	return render_template('register.html')

@app.route("/")
def subscribers():
	db = Database("one_a_day")
	db.connect()
	subscribers = db.getSubscribers()
	return render_template(
		'subscribers_interests.html',
		subscribers=subscribers)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')