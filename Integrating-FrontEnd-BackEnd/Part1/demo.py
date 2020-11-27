from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':
		# We can add a message, just for be sure we are in index
		return render_template('index.html')
	else:
		username = request.form['username']
		password = request.form['password']
		if username == 'Sebastian' and password == "sebas123":
			message = model.showUserColor('Sebastian')
			return render_template('home.html', message = message)
		else:
			error_message = 'Try again!'
			return render_template('index.html', message = error_message)

@app.route('/about', methods = ['GET'])
def aboutme():
	return render_template('about.html')

if __name__ == '__main__':	
	app.run(port = 3200, debug = True)