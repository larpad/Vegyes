from flask import Flask, redirect, url_for, render_template, request, session, send_file

from web.szamolo import Szamolo
from database.database import Database
from io import BytesIO



class tanora:
        def __init_(self, ora,cseng_be,cseng_ki):
            self.ora = ora
            self.cseng_be = cseng_be
            self.cseng_ki = cseng_ki
        def get_name(self):
            return f"{self.ora}. óra"
class lista_tanora:
        def __init__(self):
            self.lista = []
        def add(self, p_tanora):
            self.lista.append(p_tanora)

lista_tanora_arany = lista_tanora()



app = Flask(__name__, template_folder='templates')
app.secret_key = "Hablaty"
"""
DB = Database()
DB.start()
print(DB.select_fajl(12))
"""
@app.route("/")
def index():
    user_name = " - N/A -"
    if "user_name" in session:
        user_name = session["user_name"]
    return render_template("index02.html", userneve= user_name)


@app.route("/<name>", methods=["POST", "GET"])
def page_none(name):
    user_name_init = '0-0'
    user_name = user_name_init

    if "user_name" in session:
        user_name = session["user_name"]

    bigname = name.upper()

    if bigname == 'JANI':
        return f"<h1>Szia Jani!</h1>"

    elif bigname == 'SZ':
        sz = Szamolo()
   #     sz.szamol()

        return render_template("szamolo.html", cim="Egy kis számolás", szoveg="Nos akkor neki esünk a számolásnak...")

    elif bigname == 'LAP':
        return render_template("lap.html", cim="Fontos lap", szoveg="Érdekes olvasmány...")

    elif bigname == 'KIMUTATAS':
        return render_template("kimutatas.html", cim="Egy fontos kimuttás", szoveg="Kezdődjék a kimutatás...",
                               nevek=["Jani", "Peti", "Karcsi"])
    elif bigname == 'USER':
        if "user_name" != user_name_init:
            return render_template("user.html", userneve=user_name)
        else:
            return render_template("login.html")
    elif bigname == 'UPLOAD':
        if request.method == "POST":
            nev = request.form["nev"]
            session["user_name"] = nev
            return redirect(url_for("index"))
        else:
            return render_template("upload.html")

    elif bigname == 'DBFILE':
        DB = Database()
        if request.method == "POST":
            file = request.files["file"]
            if not file:
                return render_template("db_file.html", fajlok=DB.select_fajl_list())

            DB.insert_fajl(file.filename, file.read())
            return render_template("db_file.html", fajlok=DB.select_fajl_list() )
        else:
            return render_template("db_file.html", fajlok=DB.select_fajl_list() )

    elif bigname == 'LOGIN':
        if request.method == "POST":
            nev = request.form["nev"]
            session["user_name"] = nev
            return redirect(url_for("index"))
        else:
            return render_template("login.html")

    elif bigname == 'LOGOUT':
        if "user_name" != user_name_init:
            session.pop("user_name", None)
        return redirect(url_for("index"))

    else:
        return f"Hát te ki vagy?: <h1>{name}!</h1>"


@app.route("/<name1>/<name2>")
def page_nn(name1,name2):
    return f"Jani: <h1>{name1} -> {name2}</h1>"

@app.route("/<name1>/<name2>/<name3>")
def page_nnn(name1, name2, name3):
    bigname1 = name1.upper()
    bigname2 = name2.upper()
    bigname3 = name3.upper()

    if bigname1 == 'DBFILE':
        if bigname2 == 'FILES':
            #return f"<h1>Szia {name3}!</h1>"
            DB = Database()
            #print( DB.select_fajl(name3))
            id, file_name, blob = DB.select_fajl(name3)

            return send_file(BytesIO(blob), attachment_filename=file_name, as_attachment= False )

#            return f"Jani: <h1> ::: {id} -> {file_name} -> {file_name}</h1>"

        else:
            return f"Jani: <h1> ::: {bigname1} -> {bigname2} -> {name3}</h1>"
    else:
        return f"Jani: <h1> ::: {name1} -> {name2} -> {name3}</h1>"

@app.route("/<name1>/<name2>/<name3>/<name4>")
def page_nnnn(name1, name2, name3, name4):
    DB = Database()
    bigname = name4.upper()

    print (name1, name2, name3, name4)

    if bigname == 'DELETE':
        print(name3)
        DB.delete_file(name3)
    return render_template("db_file.html", fajlok=DB.select_fajl_list())

#    return f"Jani: <h1> :::: {name1} -> {name2} -> {name3}-> {name4}</h1>"


if __name__ == "__main__":
    app.run(debug = True)

# --------------------------------------------------------
"""
@app.route("/admin")
def admin():
    return redirect(url_for("jani", nome="A te Adminod"))
"""