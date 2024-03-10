import json

class Tanulo:
    oid = 0

    def __init__(self):
        Tanulo.oid = Tanulo.oid + 1
        self.id = Tanulo.oid
        self.nev = ""
        self.omazon = ""
        self.sorsz = 0

    def set(self, sorsz, omazon, nev):
        self.nev = nev
        self.sorsz = sorsz
        self.omazon = omazon

    def get(self):
        return f" {self.id}  {self.sorsz} {self.omazon} {self.nev}"

    def get_list(self):
        return [self.id, self.sorsz, self.omazon, self.nev]

    def get_json(self):

        l_dictionary = { "id": self.id, "sorsz": self.sorsz, "omazon": self.omazon, "nev": self.nev}

        l_json = json.dumps(l_dictionary, indent=4)

        return l_json