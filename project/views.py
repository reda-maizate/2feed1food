from . import app
from flask import render_template
import matplotlib.pyplot as plt

import plotly.express as px

def test():
    
#     df = px.data.gapminder().query("country=='Canada'")
#     fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    return ""


def homePage():
    return render_template("index.twig")


@app.route('/test')
def index():
    return test()




@app.route('/')
def index2():
    return homePage()

