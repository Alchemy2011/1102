from flask import Flask, render_template, redirect, abort, url_for
from flask_script import Manager
from flask import make_response

app = Flask(__name__)
app.debug = True

manager = Manager(__name__)


@app.route('/')
def index():
    return '<h1>Index</h1>'


@app.route('/hello/')
def hello():
    return 'Hello World!'


@app.route('/name/<name>')
def showName(name):
    return 'Name %s' % name


@app.route('/post/<int:id>')
def show_post_id(id):
    return 'Post_id %s' % (id * 2)


@app.route('/redir/')
def redir():
    return redirect('/hello/')


@app.route('/abort/')
def abt():
    return abort(401)


@app.route('/world/')
def world():
    return redirect(url_for('hello!'))

@app.route('/cookie/')
def cookie():
    response = make_response('hello cookie',200)
    response.set_cookie()


if __name__ == '__main__':
    # app.run()
    manager.run()
