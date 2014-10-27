from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def show_creepy_form():
	return render_template("main.html")

@app.route('/creepy')
def is_it_creepy():
	your_age = request.args.get("your_age")
	other_age = request.args.get("other_age")
	print your_age
	print other_age



	your_age = int(your_age)
	other_age = int(other_age)
	if other >= (your_age/2 + 7):
		return render_template("creepy.html", your_age=your_age, other_age=other_age
			)
	else:
		return render_template("creepy.html", your_age=your_age, other_age=other_age)


if __name__ == '__main__':
    app.run(debug=True)