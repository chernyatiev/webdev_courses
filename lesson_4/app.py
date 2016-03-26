from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)



posts = {
         1 : {"id" : 1, "title" : "My first post", "body" : "Some text"},
         2 : {"id" : 2 , "title" : "My second post", "body" : "Another text"}}


@app.route('/')
def index():
    return 'Hello'


@app.route('/posts')
def all_posts():
    return render_template('posts.html', posts = posts.values())

@app.route('/post/<post_id>')
def post(post_id):
    try:
        post_id = int(post_id)
    except:
        return 'Not found'
    post = posts[post_id]
    if post:
        return render_template('post.html', post=post) 
    else:
        return 'Not found'


@app.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title=request.form['title']
        body=request.form['body']
        id = max(posts.keys())+1
        posts[id] = {"id" : id, "title": title, "body" : body}
        return redirect(url_for('all_posts'))
    else:
        return render_template('form.html')


@app.route('/search')
def search():
    query = request.args.get('q') 
    return render_template('search.html', query=query)

if __name__ == "__main__":
    app.debug = True
    app.run()

