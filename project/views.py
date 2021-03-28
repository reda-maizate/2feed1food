from . import app
from flask import render_template
import matplotlib.pyplot as plt

def test():
    data = [1,2,3,2,5]
    data2 = [2,4,3,6,6]
    return print(type(plt.plot(data,data2)))






def test2():
    return render_template("index.html")


@app.route('/test')
def index():
    return test()




@app.route('/test2')
def index2():
    return test2()




