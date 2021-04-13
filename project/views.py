from . import app
from flask import render_template, jsonify, request

from .python.homepage import homePage
from .python.mongoosastic.mongoosastic import *
from .python.ajax.searchBar import *


@app.route('/')
def home():
    return homePage()


@app.route('/nosql')
def hello_word():
    return "Hello non"


@app.route('/get', methods=["POST", "GET"])
def ajax_search():
    res = request.args.get('param')
    # return render_template("testmongo.html", res='')
    return get_item(res)


#### First version is working with Mongo

# @app.route("/index", methods=["GET"])
# def search_results():
#     query = request.args.get('q')
#     projects = db.collections.find({"product_name": query}).limit(5)
#     print(projects)
#     return render_template("index2.twig", projects=projects)

#### Second version working with Elasticsearch

@app.route("/index", methods=["POST", "GET"])
# Accés par la page /index?q
def search_results():
    query = request.args.get('q')
    a = es1.search(index="test", body={
        "from": 0, "size": 5,
        "query": {
            "query_string": {
                "default_field": "product_name",
                "query": f"*{query}*",
            }
        }
    })
    return render_template("index2.twig", projects=a)
