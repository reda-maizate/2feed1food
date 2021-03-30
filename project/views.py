from . import app
from .python.homepage import homePage
from .python.ajax.test import *
from flask import request


@app.route('/test')
def test():
    return test()

@app.route('/')
def home():
    return homePage()


@app.route('/test4', methods=['POST'])
def test4():
    return noName(request)
