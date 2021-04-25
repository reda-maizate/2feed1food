from flask import render_template

from notebook.mongoosastic.mongoosastic import es1


def get_product(_id):
    product = es1.search(index="off_collections", body={
        "query": {
            "ids": {
                "values": [str(_id)],
            }
        }
    })
    # return json.dumps(product)
    return render_template('blocks/beautify_product.twig', product=product['hits']['hits'][0]['_source'])
