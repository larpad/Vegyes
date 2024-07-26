import os
import json
import xlrd

class Fajl:
    def __init__(self,pID,pPath):
        self.ID = pID
        self.Path = pPath
        """
        lExcel = xlrd.open_workbook_xls(pPath)
        lSheet = lExcel.sheet_by_index(0)
        lData = {}
        j = 1
        for i in range(4, 13):
            key = str(lSheet.cell(i, 3).value) #.decode('utf-8')  # cell_value(i, 3) #.encode('utf-8').decode('utf-8')
            value = str(lSheet.cell(i, 7).value)  # .encode('utf-8').decode('utf-8')
            #      lData.append([key,value])
            lData[key] = value
            j += 1

        self.ID = pID
        self.Path = pPath
        self.InditoSzamlaszam = lData['Indító számlaszám']
        self.TranzakciAzonosito = lData['Tranzakció azonosító']
        self.RogzitesDatuma = lData['Rögzítés dátuma']
        self.TranzakcioAllapota = lData['Tranzakció állapota']
        self.TranzakcioMegnevezese = lData['Tranzakció megnevezése']
        self.EllenoldaliSzamlaszam = lData['Ellenoldali számlaszám']
        self.Osszeg = lData['Összeg']
        self.Kozlemeny = lData['Közlemény']
        self.KedvezmenyezettNeve = lData['Kedvezményezett neve:']
        """
    def toJSON(self):
#        return {"Indító számlaszám":self.InditoSzamlaszam}
        return json.dumps({"id":self.ID,"filepath":self.Path})

class FajlList:
    def __init__(self,pDirPath):
        self.DirPath = pDirPath
        lID = 0
        self.FileList = []
        for lPath in os.listdir(self.DirPath):
            lID += 1
            self.FileList.append(Fajl(lID,lPath))
    def toList(self):
        for item in self.FileList:
            print(item.toJSON())
    def toJson(self):
        return 0


def get_excel_datas(p_xls_path):
    """
        lExcel = xlrd.open_workbook_xls(p_xls_path)

        #lData = []
        #lData.append(['sheet_name', lExcel.sheet_by_index(0).name])
        lSheet = lExcel.sheet_by_index(0)
        lData = {}
        j = 1
        for i in range(4, 13):
            key = str(lSheet.cell(i,3).value) # cell_value(i, 3) #.encode('utf-8').decode('utf-8')
            value = str(lSheet.cell(i, 7).value) #.encode('utf-8').decode('utf-8')
      #      lData.append([key,value])
            lData[key] = value
            j += 1
    """
    lCE = Fajl(1, p_xls_path)
    print(lCE.Path)
    return lCE
"""
{'Indító számlaszám': '11773377-30633108', 'Tranzakció azonosító': '23550579917', 'Rögzítés dátuma': '2023.06.09.', 'Tranzakció állapota': 'Végrehajtva', 'Tranzakció megnevezése': 'Belföldi forint átutalás', 'Ellenoldali számlaszám': '11773377-02068699', 'Összeg': '15.000', 'Közlemény': 'Losonczi Dorina 2022/23Osztálypénz - Bocsánat', 'Kedvezményezett neve:': 'KNYK Baksa Kálmán Gimnázium'}
"""