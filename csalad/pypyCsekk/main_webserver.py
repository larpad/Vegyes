import os

import xlrd
#from PyPDF2 import *
from fpdf import *
from flask import *
import requests
import json

from bl_pdf import *



# --------------------------------------------------------

# --------------------------------------------------------
class Webserver:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route("/")
        def route_index():
            #    return render_template("index.html")
            return render_template("kozoskoltseg.html")

        @self.app.route("/test", methods = ['GET','POST','PUT','PATCH','DELETE'])
        #@app.route("/test", methods = ['GET','POST'])
        def route_test():
            content_type = ''
            lData = 'ERROR'

            """
            print("------------------------------------")
            headers = request.headers
            for item in headers:
                print(item, headers.get(item))
        
            print("------------------------------------")
        
            content_type = request.headers.get('Content-Type')
            accept = request.headers.get('Accept')
            print(content_type)
            print(accept)
        
            args = request.args.to_dict()
            for item in args:
                print(item, args.get(item))
        
            print(request.data)
            print("------------------------------------")
            print("------------------------------------")
            """

            if request.method == 'GET':
                print("GET")

                if (content_type == 'application/json'):
                    lData = "GET -> " + json.loads(request.data)

                elif (accept == 'application/json'):
                    lData = "GET -> " + json.loads(request.data)

                else:
                    lData = "GET -> NON JSON"

            elif request.method == 'POST':
                print("POST")
                print(request.data)
                lData = {"kozoskoltseg" : { "tipus" : "Válasz"
                                           ,"pdf"  : "PDF"}}


                json.dumps(lData)



            else:
                lData = "ELSE METHOD "

            print(lData)
            return lData

        @self.app.route("/create_file", methods = ['GET','POST'])
        def create_file():
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json'):
                print("JSON")

                data = json.loads(request.data)
                #        data = request.json
                print(data);
                return "JSON"
            else:
                print("NON JSON")
                print(request.form.get("tipus"));
                file = request.files["pdf"]

                file.save(osecure_filename(file.filename))

            #        filename = secure_filename(file.filename)
        #        session["id"] = filename
        #        file.save(os.path.join('UPLOAD', filename))
        #        return redirect(url_for('uploaded', filename=filename))

                return send_file(osecure_filename(file.filename))
        #        return "NON JSON"

            """
            return "pity"
            excel = request.form.get('excel')
        
            print(l_tipus);
            print("00");
        
            data_tipus = "none"
        
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json'):
        
                print("01");
                data = json.loads(request.data)
        #        data = request.json
                print(data);
        
                print("02");
                data_tipus = data.get('tipus')
                print(data_tipus);
            else:
                return "Pity"
        
            if data_tipus == "kozoskoltseg":
                print("03");
                print("Közösköltség");
                file_excel = data.get('excel')
                file_pdf = data.get('pdf')
                print("04");
                print(file_pdf);
                print("05");
                print(request);
        
                print("06");
                for item in data.get('pdf'):
                    print(item)
        
                print("07");
                print(len(data));
                print("08");
                print(json.dumps(data, indent=2));
            """


            """
            print(excel);
            pdf = request.form.get('pdf')
            print(pdf);
        
            content_type = request.headers.get('Content-Type')
            print(content_type)
        
            if (content_type == 'application/json'):
                data = request.json
                data_tipus = data.get('tipus')
        
        #        data_data = json.loads(request.json)
        #        print(data_data)
        
                with open('json_data.json', 'w') as outfile:
                    outfile.write(data.get('pdf'))
        
                data_pdf = data.get('pdf').get('name')
                print(data_pdf)
                data_excel = data.get('excel')
                print(data)
                or file in request.files.getlist():
                    file.save(os.path.join(uploads_dir, secure_filename(file.name)))f
                print(request.form['tipus'])
        #        print(data_pdf)
        #        print(data_excel)
        #        path_pdf = 'C:\\Users\\Apu\\Desktop\\FizetendőSzámla\\110-GMK-Árpika-s23001001050.pdf'
        #        path_excel = 'C:\\Users\\Apu\\Desktop\\FizetendőSzámla\\10-GMK-Árpika-UTALÁS-20231009_visszaigazolas_24277465335.xls'
        
        #        pecseteles(path_pdf,path_excel)
                return data_tipus
            return "Pacal"
            #return send_file("pecsetelt.pdf")
            """
            a = jokes()
            return "pity" #data
        @self.app.route("/ebed_load", methods = ['POST'])
        def ebed_load():
            print("ebed_load")
            return render_template("ebed.html")

        @self.app.route("/takaritas")
        def route_takaritas():
            return render_template("takaritas.html")

        @self.app.route("/takaritas_post", methods = ['GET'])
        def route_takaritas_post():
        #    f_datum = request.form.get("datum")
            f_datum = request.args.get("datum")
            create_pdf_takaritas(f_datum)

            print("01")
            return render_template("takaritas_post.html", pdatum = f_datum)



        @self.app.route("/kozoskoltseg")
        def route_kozoskoltseg():
            return render_template("kozoskoltseg.html")

        @self.app.route("/kozoskoltseg_load", methods = ['POST'])
        def route_kozoskoltseg_load():
            print("01")
            f_excel = request.files["excel"]
            f_excel.save(f_excel.filename)

            f_pdf = request.files["pdf"]
            f_pdf.save(f_pdf.filename)

            pecseteles(f_excel.filename,f_pdf.filename)

        #    return render_template("kozoskoltseg_loaded.html", pnev = f.filename, pa = 'a')
            return send_file("pecsetelt.pdf")
    def run(self):
        self.app.run()
    def kac(self):
        print('KacKac')