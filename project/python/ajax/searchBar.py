import json
import random

import numpy
from numpy import *

import pymongo
from flask import render_template
from notebook.mongoosastic.mongoosastic import es1

def random_color():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    return hex_number


def get_item(request):

    param = request.form.get('param')
    data_cols = ['fat_100g', 'carbohydrates_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g',
                 'nutrition-score-fr_100g', 'nutrition-score-uk_100g']
    res = es1.search(index="off_collections", body={
        "from": 0, "size": 5,
        "query": {
            "query_string": {
                "fields": ["product_name"],
                "query": f"*{param}*",
            },
        },
        "fields": data_cols + ['product_name'],
        "_source": False,
    })

    jsonData = {'labels': data_cols, 'data': []}

    if len(res['hits']['hits']) > 1:
        for row in res['hits']['hits']:
            jsonData['data'].append({
                'data': list(numpy.array(list(row['fields'].values())).flatten()),
                'label': row['fields']['product_name'][0],
                'backgroundColor': str(random_color()),
            })
        return jsonData
    return {
        'error': True,
        'message': "No results found...",
    }

