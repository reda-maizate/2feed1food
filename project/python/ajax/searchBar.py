import json
import random

import pymongo

from notebook.mongoosastic.mongoosastic import es1


def random_color():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    return hex_number


def get_item(param):
    data_cols = ['fat_100g', 'carbohydrates_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g',
                 'nutrition-score-fr_100g', 'nutrition-score-uk_100g']
    res = es1.search(index="off_collections", body={
        "from": 0, "size": 100,
        "query": {
            "query_string": {
                "fields": ["product_name"],
                "query": f"*{param}*",
            },
        },
        "fields": data_cols,
    })
    row = res["hits"]["hits"][0]['_source']

    return {
        'labels': data_cols,
        'data': {
            'data': [row[key] for key in data_cols],
            'label': row['product_name'],
            'backgroundColor': str(random_color()),
        }
    }


# def get_item(param):
#     data_cols = ['fat_100g', 'carbohydrates_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g',
#                  'nutrition-score-fr_100g', 'nutrition-score-uk_100g']
#     res = es1.search(index="off_collections", body={
#         "from": 0, "size": 5,
#         "query": {
#             "query_string": {
#                 "fields": ["product_name"],
#                 "query": f"*{param}*",
#             },
#         },
#         "fields": data_cols,
#     })
#     # row = res["hits"]["hits"][0]['_source']
#
#     returned = {'labels': (data_cols,), 'data': []}
#
#     for row in res["hits"]["hits"]:
#         returned['data'].append({
#             'data': [row['_source'][key] for key in data_cols],
#             'label': row['_source']['product_name'],
#             'backgroundColor': random_color(),
#         })
#
#     return returned
