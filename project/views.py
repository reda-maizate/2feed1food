import json

from . import app
from flask import render_template, request, redirect, url_for, session

from notebook.mongoosastic.mongoosastic import *
from .python.ajax.searchBar import *


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
def search_results():
    query_fields = ["ingredients_text", "product_name"]
    data_cols = ['ingredients_text', 'brands', 'product_name', 'fat_100g', 'carbohydrates_100g', 'sugars_100g',
                 'fiber_100g',
                 'proteins_100g', 'salt_100g', 'nutrition-score-fr_100g', 'nutrition-score-uk_100g', 'energy_100g']
    query = request.form.get('query')

    optionsOrder = {}

    optionsRemove = {}
    for column in request.form:
        if column != 'query':
            specification = request.form.get(column)
            if specification in ['asc', 'desc']:
                optionsOrder[column] = specification
            if specification in [True, False]:
                optionsRemove[column] = specification

    a = es1.search(index="off_collections", body={
        "from": 0, "size": 15,
        "query": {
            "bool": {
                "must": {
                    "query_string": {
                        "fields": query_fields,
                        "query": f"*" + query + "*",
                    },
                },
                "must_not": [
                    {
                        "term": {"ingredients_text": "gluten"},
                    },
                    # {
                    #     "term": {"ingredients_text": "lait"},
                    # }
                ]
            }
        },
        "sort": optionsOrder,
        "fields": data_cols,
        "_source": False,
    })


    if a['hits']['total']['value'] <= 0:
        return "Aucune correspondance trouvée"
    return render_template("blocks/search-bar-result.twig", projects=a)




@app.route("/ai")
def ai():
    return render_template("ai.twig")
