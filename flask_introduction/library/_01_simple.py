import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to our Library!'

#{{ rendering value of some var || placement holder for variable
#{% means special command or statement of tamplate and shine?
# could be if statemenbt, or set somethhing, or anything else

#uses weinzburg for template and shine?