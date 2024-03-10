from prg import program
from scriptek import listak
from scriptek import comprehension
from fajl import szovegszamlalo
from fajl import rexi
from fajl import tablazat
from datum import ido
from database import db
# program.Program().Start()
# listak.lista()

# listak.ranlist()
# listak.gyakorisag()
# comprehension.sentece()
print(f"------------------")
# szovegszamlalo.Szamlalo()
# rexi.Rexi()
# tablazat.Tab()
# ido.Ido()
# db.Run()
for sor in db.iskola_osztaly_select():
    print(sor)


print(db.iskola_osztaly_select_id(7))

# ####
print(f"-- PROGRAM VÉGE --")

