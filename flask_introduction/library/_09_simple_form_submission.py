from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('simple_form.html')
    elif request.method == 'POST':
        return "Submitted title: {}".format(request.form['title'])


#request.form['title'] is a key for a dictionary object, form, that is found in the dict 
#eg. From simple_form.html (which calls the post method when you submit)
#<input class="form-control" name="title" placeholder="Author title"> 
#<input class = "form-control" name = "isbn" placeholder = "ISBN"
#the key is the name field!! here, it would be 'title', and 'isbn'