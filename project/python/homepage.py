from flask import render_template

def homePage():
    return render_template("index.twig")