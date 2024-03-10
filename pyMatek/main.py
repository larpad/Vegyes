import os
import random



def clear_console():
    os.system('cls')

def fomenu():
    text = """
1 Téglatest
2 Henger 
3 Gömb
4 Véletlen
5 Generál

E Eredmény lista

L Betöltés
S Mentés

X Kilépés    
    """

    Tovabb = True

    while Tovabb:
        clear_console()
        print(text)
        lValasz = input("Választás: ")

        if lValasz in ["1","2","3","4","5","e","l","s","x"]:
            Tovabb = False

    return  lValasz






def almenu():

    return """
1 Felszin
2 Térfogat 

X Vissza    
    """
def szamolo(pFomenu,pAlmenu):
    return

def menu_tegla():
    clear_console()
    print(almenu())
    menu_valaszt = input("Választás: ")
    return

def menu_henger():
    return

def menu_gomb():
    return

def menu_veletlen():
    return

def menu_general():
    return

def menu_eredmeny_lista():
    return

def menu_save():
    return

def menu_load():
    return
#.........................................................................................
Tovabb = True

lista_eredmeny =[]

while Tovabb:
    clear_console()
    print("*** Ez e fontos program ***")

    fomenu_valaszt = fomenu()

    if fomenu_valaszt in ["1","2","3"]:
        almenu_valaszt = almenu()
        if almenu_valaszt in ["1","2"] :
            szoveg = szamolo(fomenu_valaszt,almenu_valaszt)
            if szoveg != "":
                lista_eredmeny.append(szoveg)
    elif menu_valaszt == "4":
        szoveg = szamolo(menu_valaszt, 0)
        szoveg = szamolo(fomenu_valaszt, almenu_valaszt)
        if szoveg != "":
            lista_eredmeny.append(szoveg)

    elif menu_valaszt == "5":
        szoveg = menu_veletlen()
        lista_eredmeny.append(szoveg)

    elif menu_valaszt == "5":
        szoveg = menu_general()
        lista_eredmeny = menu_general()

    if menu_valaszt == "5":
        szoveg = menu_eredmeny_lista()
    if menu_valaszt == "5":
        szoveg = menu_save()
    if menu_valaszt == "5":
        szoveg = menu_load()

    if menu_valaszt == "x":
        Tovabb = False
