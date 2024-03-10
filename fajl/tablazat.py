import os
import subprocess
def Tab():
    Termekek = [
         ["Megnevezés","Mértékegység","Egységár","Mennyiség"],
         ["Tojás", "darab", "30",  "4"],
         ["Alma", "kg", "147", "2"],
         ["Tej", "liter", "310", "12"],
         ["Kenyér", "kg", "230", "4"]
    ]
    MindOsszesen = 0
    FileName = r"C:\Users\Apu\Desktop\nyugta.csv"
    PathProgram = r"C:\Program Files\LibreOffice\program\scalc.exe"
    # with open(FileName, "w", encoding='utf8') as file: #Excel helyett mindenki más
    with open(FileName, "w") as file : # Excel
        for elem in Termekek:
            if elem[0] != "Megnevezés":
                Osszesen = int(elem[2])* int(elem[3])
                MindOsszesen += Osszesen
                file.writelines(f"{elem[0]};{elem[1]};{elem[2]};{elem[3]};{Osszesen}\n")

            else:
                file.writelines(f"{elem[0]};{elem[1]};{elem[2]};{elem[3]};Összesen\n")
        file.writelines(f"Mindösszesen;;;;{MindOsszesen}\n")
    os.startfile(FileName)
    subprocess.run(["C:\Program Files\LibreOffice\program\scalc.exe",FileName])
    # os.system("start PathProgram) # {FileName}")

