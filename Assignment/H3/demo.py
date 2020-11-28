from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		username = request.form['username']
		password = request.form['password']
		if username == 'admin@mail.com' and password == "admin123":
			return render_template('dashboard.html', message = 'Welcome back')
		elif username == 'poe@mail.com' and password == "allanPoe":
			return render_template('dashboard.html', message = 'Welcome back')
		else:
			error_message = 'Try again!'
			return render_template('index.html', message = error_message)

@app.route('/about', methods = ['GET'])
def aboutme():
	return render_template('about.html')

@app.route('/terms', methods = ['GET'])
def termsOfUse():
	return render_template('termsOfUse.html')

@app.route('/privacy', methods = ['GET'])
def privacy():
	return render_template('privacy.html')



if __name__ == '__main__':	
	app.run(port = 3200, debug = True)