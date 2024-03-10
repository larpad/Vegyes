from osztaly import Osztaly
import json

class Iskola:
    def __init__(self):
        self.osztalyok = []
    def __add_osztaly(self, osztaly):
        self.osztalyok.append(osztaly)

    def create_osztaly(self):
        l_osztaly = Osztaly()
        self.__add_osztaly(l_osztaly)
        return l_osztaly

    def __str__(self):
        text = "Osztályok\n"

        for osztaly in self.osztalyok:
            text = f"{text}{osztaly.get()}"
        return text

    def get_list(self):

        l_gyerekek = []
        for osztaly in self.osztalyok:
            for gyerek in osztaly.get_list():
                l_gyerekek.append(gyerek)

        return l_gyerekek

    def get_xml(self):

        l_xml = ""

        return l_xml

    def get_json(self):

        l_json = ""

        return l_json