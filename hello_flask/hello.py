# coding: utf-8
from flask import Flask, redirect, abort, url_for, request, \
    make_response, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# app.debug = True
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return '<h1>Index</h1>'


@app.route('/hello/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def showUserName(name):
    return 'User %s' % name


@app.route('/post/<int:post_id>')
def showPostId(post_id):
    return 'Post %d' % post_id


@app.route('/about/')
def about():
    return 'The about page'


@app.route('/post2/<int:post_id>')
def showPostId2(post_id):
    return 'Post %d' % (post_id * 2)


@app.route('/redir/')
def redir():
    return redirect('/login/')


@app.route('/login/')
def login():
    return abort(401)


@app.route('/world/')
def world():
    # return redirect('/hello/')
    # return redirect(url_for('hello_world'))
    # return redirect(url_for('showUserName', name='liqirong'))
    return redirect(url_for('showPostId', post_id=100))


# 请求上下文
@app.route('/useragent/')
def userAgent():
    user_agent = request.headers.get('User-agent')
    return '<p>Your browser is %s</p>' % user_agent


# 响应的两种方式
@app.route('/bad/')
def bad():
    return '<h1>Bad Request</h1>', 400


# 视图函数，返回响应对象
@app.route('/response/')
def response():
    resp = make_response('<h1>Bad Request</h1>', 400)
    return resp


# 如果返回的是响应对象，那么就可以设置cookie
@app.route('/cookie/')
def cookie():
    resp = make_response('set cookie')
    resp.set_cookie('name', 'mysite')
    print request.cookies.get('name')
    return resp

@app.route('/hellotemplate/')
def helloTemplate():
    return render_template('hello.html')

@app.route('/hellotemplate/<name>')
def helloName(name):
    return render_template('helloname.html',name=name)

@app.route('/iftemplate/<name>')
def ifTemplate(name):
    return render_template('if.html',name=name)
# 解除硬编码不会

@app.route('/for/')
def forTemplate():
    return render_template('for.html')

@app.route('/macro/<a>')
def macrotemplate(a):
    return render_template('macro.html', A=a)

@app.route('/macro2/<a>')
def macro2template(a):
    return render_template('macro2.html', A=a)

@app.route('/include/<a>')
def includetemplate(a):
    return render_template('include.html', A=a)

@app.route('/extend/')
def extendtemplate():
    return render_template('extend.html')

@app.route('/bootstrap/<name>')
def bootstraptemplate(name):
    return render_template('bootstrap2.html', name=name)

if __name__ == '__main__':
    # app.run()
    manager.run()
