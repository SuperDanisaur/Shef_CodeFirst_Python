#app.py
from flask import Flask
import mymodule

app= Flask("demoApp")

@app.route("/")
def say_hello():
	return str(mymodule.cosine(1))

app.run(debug=True)
