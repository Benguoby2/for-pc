from flask import Flask, url_for, request
app = Flask(__name__)
"""
@app.route("/")
def hello_world():
    return "Indes page"

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/user/<username>")
def show_user_profile(username):
    return "user is %s" % username

@app.route('/post/<string:post_id>')
def show_post(post_id):
    return 'Post %s' %post_id

@app.route('/project/')
def project():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print (url_for('hello'))
    print (url_for("about"))
    print (url_for('project', next='/'))
    print (url_for('project', username='John Doe'))
"""
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login'
    else:
        show_the_login_form()
def do_the_login():
    return 'login'
def show_the_login_form():
    return'form'"""
"""
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
"""
from flask import abort, redirect, url_for, session

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'