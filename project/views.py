from . import app
from .python.homepage import homePage
from .python.ajax.test import *
from .python.mongoosastic.mongoosastic import *
from flask import render_template, jsonify

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

#### First version is working with Mongo

# @app.route("/index", methods=["GET"])
# def search_results():
#     query = request.args.get('q')
#     projects = db.collections.find({"product_name": query}).limit(5)
#     print(projects)
#     return render_template("index2.twig", projects=projects)

#### Second version working with Elasticsearch

@app.route("/index", methods=["GET"])
# Accés par la page /index?q
def search_results():
    query = request.args.get('q')
    a = es1.search(index="test", body={
                                       "from": 0, "size": 5,
                                        "query": {
                                            "match":
                                                {"product_name": query,
                                                 }
                                        }
    })
    return render_template("index2.twig", projects=a)
