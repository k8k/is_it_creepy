from flask import Flask, jsonify, render_template, request
import os


SECRET_KEY 		= os.environ.get("FLASK_SECRET_KEY", "development")
# DATATBASE_URL	= os.environ.get("DATATBASE_URL", "postgresql:///hackbright")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def show_creepy_form():
	return render_template("main.html")

@app.route('/creepy')
def is_it_creepy():
	your_age = request.args.get("your_age", type=int)
	other_age = request.args.get("other_age", type=int)
	print your_age
	print other_age

	is_creepy = (other_age < (your_age/2 + 7))
		
	return jsonify(is_creepy=is_creepy)


if __name__ == '__main__':
	PORT = int(os.environ.get("PORT",5000))
	DEBUG = "NO_DEBUG" not in os.environ

	app.run(debug=DEBUG, host="0.0.0.0", port=PORT)