"""Ez az Adatbázis modul! van benne adatbázis objektum, meg minden más is, amit még nem tudok elképzelni!"""
class DB:
    """Ez az Adatbázis Object"""
    NEVEM = "Adatbázis"
    LIST = []
    def __init__(self):
        self.NEVEM = f"Az én nevem, az én nevem : {self.NEVEM}"

        self.LIST.append(TABLE("Személyek"))
        self.LIST.append(TABLE("Média"))
        self.LIST.append(TABLE("Előadás"))
        # self.LIST.append("Nyaffancs")
        # self.LIST.append("Puffancs")
        # self.LIST.append("Toppancs")

    def start(self):
        """Ez az adatbázis indító függvény"""
        print("DB Start")
        for sor in self.LIST:
            sor.Kiir()

class TABLE:
    NEVEM = "Tábla"
    LIST = []
    def __init__(self, pNEV):
        self.NEVEM = pNEV
    def getNev(self):
        return self.NEVEM
    def Kiir(self):
        print("A tábla neve : ",self.NEVEM)

