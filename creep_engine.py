from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)

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
	app.run(debug=True, host="0.0.0.0", port=PORT)