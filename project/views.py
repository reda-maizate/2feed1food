from flask import request

from . import app
from .python.GET.get_product import *
from .python.ajax.searchBar import *
from .python.ajax.search_specs import *
from .python.ajax.group_by import *


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


@app.route("/score")
def get_score_route():
    return group_by()


@app.route("/score/ajax", methods=["POST"])
def get_score_ajax_route():
    grade = request.form.get("grade")
    origin = request.form.get("origin")
    return get_by_score(grade, int(origin))
