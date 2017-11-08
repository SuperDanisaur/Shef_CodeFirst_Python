from flask import Flask
app = Flask("Week3ChallengeApp")
@app.route("/")
def index():
#Fallback root path request handler so that the user doesn't get greeted with a nasty 404 not found page#
	return "It works!"
@app.route("/ambassador/<name>")
def get_ambassador(name):
	name = name.capitalize()
	if name == "Pauline" or name == "Lakshika":
		return f"{name} is our awesome #ShefCodeFirst ambassador! Go {name}!"
	else:
		return "We don't know who s/he is! Maybe you typed in the wrong name?"
@app.route("/instructor/<name>")
def get_instructors(name):
	instructors = ["Chris", "Darren", "Nina", "Tania"]
	name = name.capitalize()
	if name in instructors:
		return f"{name} is our awesome #ShefCodeFirst instructor! <3"
	else:
		return "We can't find this instructor! Maybe you typed in the wrong name?"
app.run(debug=True)