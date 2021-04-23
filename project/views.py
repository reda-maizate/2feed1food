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
    res = request.args.get('param')
    # return render_template("testmongo.html", res='')
    return get_item(res)

@app.route("/", methods=["POST", "GET"])
def search_results():
    query = request.args.get('q')
    results = es1.search(index="off_collections", body={
        "from": 0, "size": 20,
        "query": {
            "query_string": {
                "fields": ["ingredients_text", "product_name"],
                "query": f"*{query}*",
            }
        }
    })
    return render_template("index.twig", results=results)
