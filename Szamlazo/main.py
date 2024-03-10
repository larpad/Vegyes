def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


class Termek:
    ID = 0,
    Megnevees = ""
    Egysegar = 0.0

    def __init__(self, pID, pMegnevees, pEgysegar):
        self.ID = pID
        self.Megnevees = pMegnevees
        self.Egysegar = pEgysegar


class Lista_Termek:
    Lista = []





class Partner:
    ID = 0
    Nev = ""
    IRSZ = ""
    Telepules = ""
    Cim = ""

    def __init__(self, pID, pNev, pIRSZ, pTelepules, pCim):
        ID = pID
        Nev = pNev
        IRSZ = pIRSZ
        Telepules = pTelepules
        Cim = pCim

class Lista_Partner:
    Lista = []

    def show(self):
        self.menu()

    def menu(self):
        print("""
        ------------------------------------
        ---- Számlázó ----------------------
        ------------------------------------
        0 Főmenü
        1 Új számla
        2 Partnertörzs
        2 Terméktörzs

        """)


class Program:
    Termekek = Lista_Termek()
    Partnerek = Lista_Partner()

    def start(self):
        menu = "0"
        while not (menu in ["x","X"]):
            self.fomenu()
            if menu == "3":
                Partner.show()


    def fomenu(self):
        menu = "0"
        while not(menu in ["0","1","2","3","x","X"]):
            print("""
------------------------------------
---- Számlázó ----------------------
------------------------------------
0 Főmenü
1 Új számla
2 Partnertörzs
3 Terméktörzs
x Kilépés
""")
            menu = input("VÁlasztott menüpont: ")
        return menu

PRG = Program()
PRG.start()