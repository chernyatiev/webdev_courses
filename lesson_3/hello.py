from flask import Flask
app = Flask(__name__)
from flask import render_template

users = {1 : "Sasha", 2 : "Dima", 3 : "Tanya"}


@app.route("/index")
@app.route("/")
def index():
    return "Index page!"

@app.route("/hello/<user_id>")
def my_hello(user_id):
    try:
        user_id = int(user_id)
        user = users[user_id]
    except:
        return "No key"
    return "Hello, " + user

@app.route('/user')
def user():
    user = { 'nickname': 'Sasha' }
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

@app.route('/adv_user/<user_id>')
def adv_user(user_id):
    try:
        user_id = int(user_id)
        user = users[user_id]
    except:
        return "No key"
    return render_template("index.html",
        title = 'Home',
        user = user)



if __name__ == "__main__":
    app.debug = True
    app.run()
