from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	# Get request
	if request.method == 'GET':
		return render_template('index.html', message='Welcome!!')
	else:
		# Post request
		username =request.form['email']
		password = request.form['password']
		if username == 'sebastian@email.com' and password == 'sebastian':
			# Call the function in model
			message = "Successful!!"
			return render_template('home.html', message=message)
		else:
			error_message = "Wrong password"
			return render_template('index.html', message = error_message)

# About us page
@app.route('/about', methods = ['GET'])
def aboutme():
	return render_template('about.html')

# Term of Use page
@app.route('/termofuse', methods = ['GET'])
def termOfUse():
	return render_template('term_of_use.html')

# Privacy page
@app.route('/privacy', methods = ['GET'])
def privacy():
	return render_template('privacy.html')

if __name__ == '__main__':	
	app.run(port = 3200, debug = True)