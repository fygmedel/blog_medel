from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("index.html")
	#return "<h1>Hola mundo</h1>"

@app.route("/coffee")
def url_coffee():
 	tipos = [
 		"Americano",
 		"Latte"
 	]
 	return render_template("coffee.html", tipos=tipos, nombre="Café")

if __name__ == "__main__":
	app.run(debug=True)