import json

from . import app
from flask import render_template, request, redirect, url_for, session

from notebook.mongoosastic.mongoosastic import *
from .python.ajax.searchBar import *
from .python.ajax.search_specs import *


@app.route('/')
def home():
    return render_template("index.twig")


@app.route('/get', methods=["POST", "GET"])
def ajax_search():
    return get_item(request)


@app.route("/index")
def index():
    return render_template("index2.twig", projects={})


@app.route("/index/post", methods=["POST"])
def search_specs_route():
    return search_specs(request)


@app.route("/ai")
def ai():
    return render_template("ai.twig")


@app.route("/product/alone", methods=["GET"])
def get_product():
    id = request.args.get('doc')

    product = es1.search(index="off_collections", body={
        "query": {
            "ids": {
                "values": [str(id)],
            }
        }
    })
    # return json.dumps(product)
    return render_template('blocks/beautify_product.twig', product=product['hits']['hits'][0]['_source'])


@app.route("/max")
def get_max():
    # collections.create_index([("nutrition_grade_fr", 1)])
    col = collections.find().sort([("nutrition_grade_fr", -1)])

    for doc in col:
        return json.dumps(doc)

# index="off_collections", body={
#         "from": 300, "size": 10,
#         "sort": [
#             {
#                 "nutrition_grade_fr": "desc",
#             },
#             {
#                 "nutrition-score-fr_100g": "desc",
#             },
#             {
#                 "nutrition-score-uk_100g": "desc",
#             }
#         ]
#     })
