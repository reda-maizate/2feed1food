from . import app
from flask import render_template
import matplotlib.pyplot as plt

@app.route('/test')
def test():
    data = [1,2,3,2,5]
    data2 = [2,4,3,6,6]
    return print(type(plt.plot(data,data2)))


@app.route('/')
def index():
    return render_template("index.html")
