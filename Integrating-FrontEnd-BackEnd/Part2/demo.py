from flask import Flask, render_template, request, session, redirect, \
	url_for, g
import model

app = Flask(__name__)
# Secret Key
app.secret_key = '\xf2\xe8\xc6\xdc\x912\xa4\x05p\xb3\x9f\xf1\x8a\xf1\x05\x0c\xcc\xfbv\xd2\xf2\xbb\xcd'

# Session's
username = ''
user = model.checkUsers()

@app.route('/', methods = ['GET', 'POST'])
def home():
	if 'username' in session:
		g.user = session['username']
		return render_template('dashboard.html')
	else:
		return render_template('login.html')
		# return render_template('login.html', message='Login in this page or signup')

	# if request.method == 'GET':
	# 	return render_template('index.html')
	# else:
	# 	username = request.form['username']
	# 	password = request.form['password']
	# 	# Using the model
	# 	dbPassword = model.checkPass(username)

	# 	if password == dbPassword:
	# 		return render_template('dashboard.html', message = 'Welcome back')
	# 	else:
	# 		error_message = 'Try again!'
	# 		return render_template('index.html', message = error_message)

# About me section
@app.route('/index', methods = ['GET'])
def index():
	return render_template('index.html')

# About me section
@app.route('/about', methods = ['GET'])
def aboutme():
	return render_template('about.html')

# Terms of use section
@app.route('/terms', methods = ['GET'])
def termsOfUse():
	return render_template('termsOfUse.html')

# Privacy section
@app.route('/privacy', methods = ['GET'])
def privacy():
	return render_template('privacy.html')

# Sign Up
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'GET':
		message = 'Please, sign up first'
		return render_template('signup.html', message = message)
	else:
		username = request.form['username']
		password = request.form['password']
		message = model.signup(username, password)
		return render_template('signup.html', message = message)

# Login 
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		session.pop('username', None)
		areYouUser = request.form['username']
		pwd = model.checkPass(areYouUser)
		if request.form['password'] == pwd:
			session['username'] = request.form['username']
			return redirect(url_for('home'))
	else:
		return render_template('login.html', message = 'Not a user')

# Get the session
@app.route('/getsession')
def getsession():
	if 'username' in session:
		return session['username']
	else:
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	return render_template('index.html')

@app.before_request
def before_request():
	g.username = None
	if 'username' in session:
		g.username = session['username']

if __name__ == '__main__':	
	app.run(port = 3200, debug = True)