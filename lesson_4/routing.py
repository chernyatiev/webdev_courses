from flask import Flask, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

"""
int	accepts integers
float	like int but for floating point values
path	like the default but also accepts slashes

"""



@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)



def index():
    response = make_response(render_template('index.html', foo=42))
    response.headers['X-Parachutes'] = 'parachutes are cool'
    response.set_cookie('cookie_name',value='values')
    return response

@app.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title=request.form['title']
        body=request.form['body']
        return render_template('post.html', title=title, body=body)
    else:
        return render_template('form.html')





