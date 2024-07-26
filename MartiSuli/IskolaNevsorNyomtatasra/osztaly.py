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


    def set(self, osztaly_szoveg):
        self.osztaly_szoveg = osztaly_szoveg.strip()

        revtext = self.osztaly_szoveg[::-1]
        pos = revtext.find(' - ')
        self.osztalyfonok = revtext[0:pos][::-1].strip()

        revtext =  self.osztaly_szoveg[:len(self.osztaly_szoveg)-pos-3][::-1].split('/')[0]
        revtext = revtext[:len(revtext)-5].split(' - ')[0][::-1].replace("- ","").strip()
        self.tipus = revtext

        self.kod = self.osztaly_szoveg.split('2021')[0].strip().replace("-","").strip().replace(" ","")
#       self.tipus = self.osztaly_szoveg.split('2021')[1].strip().split(' - ')[1].strip()


    def get(self):
        text = ""
        text = text + f"======================================================\n"
        text = text + f"{self.id}\n"
        text = text + f"===========\n"
        text = text + f"{self.kod}\n"
        text = text + f"===========\n"
        text = text + f"Osztályfőnök: {self.osztalyfonok} \n"
        text = text + f"Típus: {self.tipus} \n"
        text = text + f"------------------------------------------------------\n"
        for tanulo in self.tanulok:
            text = f"{text}{tanulo.get()}\n"
        text = text + f"======================================================\n"
        return text

    def __add_tanulo(self, Tanulo):
        self.tanulok.append(Tanulo)

    def create_tanulo(self):
        l_tanulo = Tanulo()
        self.tanulok.append(l_tanulo)
        return l_tanulo

    def add_tanulo(self, nev, omazon):
        l_tanulo = Tanulo()
        self.tanulo_sorsz = self.tanulo_sorsz + 1
        l_tanulo.set(self.tanulo_sorsz, omazon,nev)
        self.tanulok.append(l_tanulo)
        return l_tanulo

    def get_list(self):

        l_tanulok = []
        for tanulo in self.tanulok:
            l_egy_tanulo = [self.kod, self.osztalyfonok, self.tipus]

            for data in tanulo.get_list():
                l_egy_tanulo.append(data)

            l_tanulok.append(l_egy_tanulo)
        return l_tanulok

    def get_json(self):

        l_tanulok = []
        for tanulo in self.tanulok:
            l_egy_tanulo = [self.kod, self.osztalyfonok, self.tipus]

            for data in tanulo.get_list():
                l_egy_tanulo.append(data)

            l_tanulok.append(l_egy_tanulo)
        return l_tanulok

    def __str__(self):
        print(self.get())
