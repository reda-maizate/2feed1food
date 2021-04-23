from . import app
from flask import render_template, request, redirect, url_for

from notebook.mongoosastic.mongoosastic import *
from .python.ajax.searchBar import *

"""
@app.route('/')
def home():
    return render_template("index.twig")
"""

@app.route('/get', methods=["POST", "GET"])
def ajax_search():
    res = request.form.get('param')
    return get_item(res)

<<<<<<< HEAD
@app.route("/", methods=["POST", "GET"])
def search_results():
    query = request.args.get('q')
    results = es1.search(index="off_collections", body={
        "from": 0, "size": 20,
=======

#### First version is working with Mongo

# @app.route("/index", methods=["GET"])
# def search_results():
#     query = request.args.get('q')
#     projects = db.collections.find({"product_name": query}).limit(5)
#     print(projects)
#     return render_template("index2.twig", projects=projects)

#### Second version working with Elasticsearch

@app.route("/index")
def index():
    return render_template("index2.twig", projects={})


@app.route("/index/post", methods=["POST"])
# Accés par la page /index?q
def search_results():
    query_fields = ["image_url", "ingredients_text", "product_name"]
    data_cols = ['brands', 'product_name', 'fat_100g', 'carbohydrates_100g', 'sugars_100g', 'fiber_100g',
                 'proteins_100g', 'salt_100g', 'nutrition-score-fr_100g', 'nutrition-score-uk_100g']

    query = request.form.get('query')

    a = es1.search(index="off_collections", body={
        "from": 0, "size": 15,
>>>>>>> c8ca4d8571a1bcbf61a5f93aea0e80b2f6615585
        "query": {
            "query_string": {
                "fields": query_fields,
                "query": f"*{query}*",
            }
        },
        "fields": data_cols,
        "_source": False,
    })
<<<<<<< HEAD
    return render_template("index.twig", results=results)
=======

    return render_template("blocks/search-bar-result.twig", projects=a)
>>>>>>> c8ca4d8571a1bcbf61a5f93aea0e80b2f6615585
