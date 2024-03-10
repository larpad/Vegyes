lista = [3, 6, "alma", 17, 12, "eferfg", 66, 70, 1995]
"""print(lista)
for a in lista:
    print(a)"""
"""print(lista[:3])
print(lista[3:])
print(lista[3:7])
print(lista[-3])
print(lista[-3:])
print(lista[-3:5])
print(lista[:])
nev = "Losonczi Árpád"
print(nev)
print(nev[3:7])
i = 0
for betu in nev:
    print(i,betu)
    i=i+1
szoveg = "Aki korán kell fáradt lesz"
j = 0
for kell in szoveg:
    if kell=="k":
        j=j+1
print(j)"""
"""szoveg = input("Kérek egy szöveget: ")
betu = input("Kérek egy betűt: ")
h = 0
for kell in szoveg:
    if kell==betu:
     h=h+1
print(h)"""
kertbetu = 0
jó = True
while jó:
    szoveg = input("Kérek egy szöveget: ")
    if szoveg == "":
        jó = False
        break
    betu = input("Kérek egy betűt: ")
    if betu=="":
        jó = False
        break
    for adat in szoveg:
        if adat==betu:
            kertbetu=+1
    print(kertbetu)









