from flask import render_template

from notebook.mongoosastic.mongoosastic import es1


def translate_options(params):
    optionsOrder = {}

    optionsRemove = []

    for column in params:
        if column != 'query':
            specification = params.get(column)
            if specification in ['asc', 'desc']:
                optionsOrder[column] = specification
            if specification in ["true", "false"]:
                newOption = {
                    "term": {"ingredients_text": column},
                }
                optionsRemove.append(newOption)
                # optionsRemove[column] = specification
    return optionsOrder, optionsRemove


def search_specs(request):
    query_fields = ["ingredients_text", "product_name"]
    data_cols = ['ingredients_text', 'brands', 'product_name', 'fat_100g', 'carbohydrates_100g', 'sugars_100g',
                 'fiber_100g', 'proteins_100g', 'salt_100g', 'nutrition-score-fr_100g', 'nutrition-score-uk_100g',
                 'energy_100g']
    query = request.form.get('query')

    optionsOrder, optionsRemove = translate_options(request.form)

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
                "must_not": optionsRemove,
            }
        },
        "sort": optionsOrder,
        "fields": data_cols,
        "_source": False,
    })

    if a['hits']['total']['value'] <= 0:
        return "Aucune correspondance trouvée"
    return render_template("blocks/search-bar-result.twig", projects=a)
