# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: flask_start.py
# @Author: myloe
# @Time: Nov 06, 2020
# ---

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return 'Index Page'

# ========================================================================================
# 当路由路径末尾没有"/"【如：@app.route('/hello'  )】时，
# 1.网页中访问【/hello 】不会报错
# 2.网页中访问【/hello/】会报错404
# 3.当浏览器成功访问过【/hello/】后，通过浏览器再次访问【/about】时会自动补齐为【/about/】导致404问题
# 当路由路径末尾  有"/"【如：@app.route('/hello/')】时
# 1.网页中访问【/hello】会自动补齐【/】
# 2.网页中访问【/hello/】不会报错
# ######################################
# #建议路由中的路径要加上【/】结尾
# ######################################
# ========================================================================================


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/hello2/')
def hello2():
    return "hello,world2"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


if __name__ == '__main__':
    app.run(debug=True)
