#app.py
from flask import Flask, render_template

app= Flask("demoApp")

@app.route("/")
def say_hello():
	return "Hello Code First Girls people!"


"""To show instead of page no found "hello and loquepongasaqui" what you 
add after the localhost:5000/loquepongasaqui """

@app.route("/<name>")
def say_hello_with_name(name):
	return f"Hello {name}"

"""MISMA FUNCION QUE LA ANTERIOR PERO CON VIEJO FORMATO
@app.route("/old/<name>")
def say_helllo_the_old_way_with_name(name):
	return "Hello {}".format(name)
	"""

"""It shows hello and the name you put after the / 
in localhost:5000/loquepongasaqui"""
@app.route("/hello/<name>")
def say_helllo_the_old_way_with_name(name):
	return render_template("index.html",name=name)



app.run(debug=True)
