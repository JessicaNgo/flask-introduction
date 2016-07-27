import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = """
        <html>
            <h1>Welcome to our Library!</h1>
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    # build an <ul> with authors
    return ul

import os from flask 

import Flask 

app = Flask(__name__) 


@app.route('/') 
def hello_world(): 
    html = """ 
                <html> 
                    <h1>Welcome to our Library!</h1> 
                </html> 
    """ 
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"] 
    # build an <ul> with authors 
    ul = "<ul>" 
    for author in authors: 
        ul += "<li>{}</li>".format(author) 
        ul = "</ul>" 
        #not cool to do it this way, this is like 8 years ago stuff, mixing code, 
        mixing php with HTML #here we mixing python and HTML, either way it is a mess! 
        
    return ul