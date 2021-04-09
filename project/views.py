from . import app
from .python.homepage import homePage
from .python.ajax.test import *
from .python.mongo.mongo import *
from flask import render_template



@app.route('/test')
def test():
    return test()

@app.route('/')
def home():
    return homePage()

@app.route('/test4', methods=['POST'])
def test4():
    return noName(request)

@app.route('/nosql')
def hello_word():
    return "Hello non"

@app.route('/get')
def mongotest():
    res = get()
    return render_template("testmongo.html", res=res)
