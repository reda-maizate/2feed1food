from . import app
from flask import render_template, request

from .python.homepage import homePage
from notebook.mongoosastic.mongoosastic import *
from .python.ajax.searchBar import *


@app.route('/')
def home():
    return homePage()


@app.route('/nosql')
def hello_word():
    return "Hello non"


@app.route('/get', methods=["POST", "GET"])
def ajax_search():
    res = request.form.get('param')
    return get_item(res)


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
        "query": {
            "query_string": {
                "fields": query_fields,
                "query": f"*{query}*",
            }
        },
        "fields": data_cols,
        "_source": False,
    })

    return render_template("blocks/search-bar-result.twig", projects=a)
