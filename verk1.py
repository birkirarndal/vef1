from sys import argv

import bottle
from bottle import *

@route("/")
def index():
    return """
    <h2> Verkefni 1.<h2>
    <a href="/about">About</a>
    <a href="/bio">Biography</a>
    <a href="/pic">Pictures</a>
    """


@route("/about")
def jobs():
    return "Hér eru upplýsingar um Steve Jobs"

@route("/bio")
def jobs():
    return "Hér er biography frá Steve Jobs"

@route("/pic")
def jobs():
    return "Hér eru myndir frá Steve Jobs"

#run(host='localhost', port=8080)

bottle.run(host='0.0.0.0', port=argv[1])
