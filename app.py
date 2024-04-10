from flask import *

app = Flask(__name__)

@app.route("/")
def base():
    if(request.method == "GET"):
        return redirect(url_for("about"))

@app.route("/about")
def about():
    if(request.method == "GET"):
        return render_template("about.html")

@app.route("/cypher", methods=['POST', 'GET'])
def cypher():
    if(request.method == "GET"):
        return render_template("cypher.html")
    
    if(request.method == "POST"):
        print(request.form['message'])

        return render_template("cypher.html")


@app.route("/decypher")
def decypher():
    if(request.method == "GET"):
        return render_template("decypher.html")
    
    if(request.method == "POST"):
        print("call decypher function")
