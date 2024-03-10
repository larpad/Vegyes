from flask import Flask, redirect, url_for, render_template, request, session, send_file


#from web.szamolo import Szamolo
from database.database import Database
from io import BytesIO

app = Flask(__name__, template_folder='templates')
app.secret_key = "Hablaty"
"""
DB = Database()
DB.start()
print(DB.select_fajl(12))
"""
@app.route("/")
def index():
    return f"Hát te ki vagy?"


@app.route("/<name>", methods=["POST", "GET"])
def page_n1():
    return f"Hát te ki vagy?: <h1>{name}!</h1>"


@app.route("/<name1>/<name2>")
def page_n2(name1,name2):
    return f"Jani: <h1>{name1} -> {name2}</h1>"

@app.route("/<name1>/<name2>/<name3>")
def page_n3(name1, name2, name3):
    return f"Jani: <h1> ::: {name1} -> {name2} -> {name3}</h1>"

@app.route("/<name1>/<name2>/<name3>/<name4>")
def page_n4(name1, name2, name3, name4):

    return f"Jani: <h1> :::: {name1} -> {name2} -> {name3}-> {name4}</h1>"

@app.route("/<name1>/<name2>/<name3>/<name4>/<name5>")
def page_n5(name1, name2, name3, name4, name5):

    return f"Jani: <h1> :::: {name1} -> {name2} -> {name3}-> {name4}-> {name5}</h1>"


if __name__ == "__main__":
    app.run(debug = True)

# --------------------------------------------------------
"""
@app.route("/admin")
def admin():
    return redirect(url_for("jani", nome="A te Adminod"))
"""