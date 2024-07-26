from tanulo import Tanulo

class Osztaly:
    oid = 0
    def __init__(self):
        Osztaly.oid =  Osztaly.oid + 1
        self.id = Osztaly.oid
        self.tanulok = []
        self.osztaly_szoveg = ""
        self.kod = ""
        self.tipus = ""
        self.osztalyfonok = ""
        self.tanulo_sorsz = 0

    def set(self,p_id,p_tipus,p_ofo):
        self.id = p_id
        self.tipus = p_tipus
        self.osztalyfonok = p_ofo
    def get(self):
        return str(self.id) + ";" + self.tipus + ";" + self.osztalyfonok + "\n"

    def get_html(self):
        l_row_osztaly = """
        <table border = 1>
        <tr><td colspan ='2'>Osztály</td><td>Tipus</td><td colspan ='3'>Osztályfőnök</td></tr>\n
        <tr><td colspan ='2'>""" + str(self.id) + "</td><td>"  +self.tipus + "</td><td colspan ='3'>" + self.osztalyfonok + "</td></tr>\n"
        l_row_osztaly += "<tr><td></td></tr>\n"

        for l_tanulo in self.tanulok:
            l_row_osztaly += l_tanulo.get_html()

        l_row_osztaly += "</table>"


        return l_row_osztaly

    def __add_tanulo(self, Tanulo):
        self.tanulok.append(Tanulo)

    def create_tanulo(self):
        l_tanulo = Tanulo(self)
        self.tanulok.append(l_tanulo)
        return l_tanulo

    def add(self,p_tanulo):
        self.tanulok.append(p_tanulo)


    def __str__(self):
        print(self.get())

    def to_xml(self):
        l_text = "<osztaly id ='" + str(self.id) + "' tipus = '"  +self.tipus + "' osztalyfonok='" + self.osztalyfonok + "'>\n"
        for l_tanulo in self.tanulok:
            l_text += l_tanulo.to_xml()

        l_text += "</osztaly>\n"

        return l_text