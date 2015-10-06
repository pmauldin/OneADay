from db.database import Database
from datetime import datetime

from flask import (
	Flask,
	abort,
	flash,
	redirect,
	render_template,
	request,
	url_for,
)
from flask.ext.stormpath import (
	StormpathError,
	StormpathManager,
	User,
	login_required,
	login_user,
	logout_user,
	user,
)

app = Flask(__name__)

@app.route("/subs")
def subscribers():
	db = Database("one_a_day")
	db.connect()
	# db.viewSubscribers()
	subscribers = db.getSubscribers()
	return render_template(
		'subscribers_interests.html',
		subscribers=subscribers)

@app.route("/")
def login():
	return "Login Now!"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')