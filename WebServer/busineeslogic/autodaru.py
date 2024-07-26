class Machina:
    Fok = 43
    # def __init__(self):
        # self.Fok = 23
    def Fordul(self):
        print(f"Fordul a gép {self.Fok} fokot ...")

class Daru(Machina):
    Suly = 10
    Kinyulas = 5
    def __init__(self, pSuly, pKinyulas):
        self.Suly = pSuly
        self.Kinyulas = pKinyulas
    def Emel(self):
        print("Kinyúl ",self.Kinyulas, " m", "és felemel ", self.Suly, " kg")
    def Fordul(self,pFok):
        self.Fok = pFok
        print("Fordul a DARU torony",self.Fok," fokot" )



class Auto(Machina):
    Kerek = 2
    Utas  = 1
    def __init__(self, pKerek, pUtas):
        self.Kerek = pKerek
        self.Utas = pUtas
    def Mozog(self):
        print("Utazik ", self.Utas," utas ", self.Kerek, " keréken")
    def Fordul(self,pFok):
        self.Fok = pFok
        print("Fordul az AUTO balra",self.Fok," fokot" )

class AutoDaru(Auto,Daru):
    def __init__(self, pKerek, pUtas):
        self.Utas = pUtas
        self.Kerek = pKerek
        self.Suly = 15
        self.Kinyulas = 100

    def Mozog(self):
        print("Az AUTODARU Utazik ", self.Utas," utas ", self.Kerek, " keréken")
    def Fordul(self):
        print("----------------")
        # super(Auto).Mozog()
        self.Mozog()
        self.Emel()
        Daru.Fordul(self,15)
        Auto.Fordul(self,25)


