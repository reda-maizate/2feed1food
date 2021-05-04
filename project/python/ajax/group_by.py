import numpy
from flask import render_template

from notebook.mongoosastic.mongoosastic import *


def get_by_score(grade, _from=0, _size=10):
    lines = collections.find({"nutrition_grade_fr": grade}).sort([("nutrition_grade_fr", -1)]).skip(_from).limit(_size)
    return render_template('blocks/poster.twig', header=grade, cursor=lines, origin=_from)


def group_by():
    # collections.create_index([("nutrition_grade_fr", 1)])
    tableContent = ""
    vals = collections.aggregate([
        {"$match": {"nutrition_grade_fr": {"$ne": numpy.nan}}},
        {"$group": {"_id": "$nutrition_grade_fr"}},
    ])
    vals = list(vals)  # if this line doesn't exist, vals cursor is not iterable anymore after render_template ://////

    tableHeader = render_template('blocks/poster_header.twig', vals=vals)
    for val in vals:
        tableContent += get_by_score(val['_id'])

    return render_template('byScore.twig', tableHeader=tableHeader, tableContent=tableContent)
