from flask import *

from gronsfeldAlphabet import gronsfeld_cypher, gronsfeld_decypher

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
        message = request.form['message']
        key = request.form['key']
        try:
            encripted_message = gronsfeld_cypher(message, key)
        except:
            return render_template("cypher.html")

        return render_template("cypher.html", value = {
            "message": encripted_message
        })


@app.route("/decypher", methods=['POST', 'GET'])
def decypher():
    if(request.method == "GET"):
        return render_template("decypher.html", )
    
    if(request.method == "POST"):
        message = request.form['message']
        key = request.form['key']
        try:
            decrypted_message = gronsfeld_decypher(message, key)
        except ValueError:
            return render_template("decypher.html")

        return render_template("decypher.html", value = {
            "message": decrypted_message
        })
