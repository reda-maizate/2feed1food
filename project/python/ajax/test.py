from inspect import getmembers
from pprint import pprint

from flask import Flask, request, jsonify


def noName(request):
    
    dataSet = [10,3,4,5,2]
    dataCols = ['red','blue','black','white','green']

    data = request.form.get('param')

    if data == 'poire':
        dataSet = [ i + 3 for i in dataSet]
        dataCols = ['one' , 'two' , 'three' , 'four' , 'five']
    elif data == 'fraise':
        dataSet = [1 for i in range (5)]
        dataCols = ['a' , 'b' , 'c' , 'd' , 'e']

    return {
        'data' : dataSet,
        'cols' : dataCols
    }
