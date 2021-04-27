from flask import request

from notebook.mongoosastic.mongoosastic import *
from . import app
from .python.GET.get_product import *
from .python.ajax.searchBar import *
from .python.ajax.search_specs import *


@app.route('/')
def home_route():
    return render_template("index.twig")


@app.route('/get', methods=["POST"])
def ajax_search_route():
    return get_item(request)


@app.route("/index")
def index_route():
    return render_template("index2.twig", projects={})


@app.route("/index/post", methods=["POST"])
def search_specs_route():
    return search_specs(request)


@app.route("/ai")
def ai_route():
    return render_template("ai.twig")


@app.route("/product/alone", methods=["GET"])
def get_product_route():
    return get_product(request.args.get('doc'))


@app.route("/max")
def get_max_route():
    # collections.create_index([("nutrition_grade_fr", 1)])
    html = ""
    vals = collections.aggregate([
        {"$match": {"nutrition_grade_fr": {"$ne": numpy.nan}}},
        {"$group": {"_id": "$nutrition_grade_fr"}},
    ])

    for val in vals:
        lines = collections.find({"nutrition_grade_fr": val['_id']}).sort([("nutrition_grade_fr", -1)]).limit(5)
        # return str(header)
        html += render_template('blocks/poster.twig', header=val, cursor=lines)

    return render_template('byScore.twig', html=html)
    # return render_template('blocks/poster.twig', cursor=col)

    # # for doc in col:
    # #     return json.dumps(doc)
    #
    # index = es1.search(index="off_collections", body={
    #     "from": 300, "size": 10,
    #     "sort": [
    #         {
    #             "nutrition_grade_fr": "asc"
    #                 # {
    #                 #     "order": "asc",
    #                 # }
    #         }
    #         # {
    #         #     "nutrition-score-fr_100g": "desc",
    #         # },
    #         # {
    #         #     "nutrition-score-uk_100g": "desc",
    #         # }
    #     ]
    # })
