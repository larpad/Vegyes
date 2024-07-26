import re
import os
import subprocess
import zipfile
def Szamlalo():

    # pattern = r'[A-Z|a-z|á|Á|é|É|í|Í|ó|Ó|ö|Ö|ü|Ü|ű|Ű]*'
    # regex = re.compile(pattern)


    try:
        # f = open(r"C:\Users\Apu\Desktop\Gyerek a vonaton",'r', encoding='utf8')
        f = open(r"C:\Users\Apu\Desktop\Gyerek a vonaton",'r') # encoding='utf8')
        txt = f.read()
        print(txt)

    finally:
        f.close()
    #
    # print('Mondatonként : \n')
    #
    # mondatok = re.split('; |\. | \: |\?|\n',txt)
    # for mondat in mondatok:
    #     print(mondat)

    # pattern = r'[A-Z|a-z|á|Á|é|É|í|Í|ó|Ó|ö|Ö|ü|Ü|ű|Ű]*'
    # pattern = r'„'
    pattern = '\.|\!|\,|\:|\„|\”|\?|\n'

    txt_word =  re.sub(pattern, "", txt)
    print(txt_word)
    txt_word = txt_word.lower()
    words = list(set(txt_word.split()))
    words.sort()
    for word in words:
        print(word)
    # words = txt.split()
    # words.sort()

    # txtre = regex.findall(txt)
    # txtre = regex.subn('*',txt)
    # txtnew = regex.findall(txt)
    # txtre = [szo for szo in txtnew if szo != '']
    # txtre.sort()
    # txtset = list(set(txtre))

    # txtset.sort()

    txtnew = ""
    # print(mondatok)
    # print(txtre)
    # print(txtset)

    # listszo = [[szo,txtre.count(szo)] for szo in txtset]
    #
    #
    # print(listszo)

    # for szo in listszo:
    #     print(szo[0],' -> ', szo[1])
    #
    # try:
    #     f = open(r"C:\Users\Apu\Desktop\Gyerek_new.txt",'w', encoding='utf8')
    #     # f = open(r"C:\Users\Apu\Desktop\Gyerek_new.txt",'w')
    #     txt = f.write(txt)
    #     # for szo in listszo :
    #     #     f.write(f"{szo[0]} ->  {szo[1]}\n")
    #     # os.system(r"start C:\Users\Apu\Desktop\Gyerek_new.txt")
    # finally:
    #     f.close()
    #
    # with open(r"C:\Users\Apu\Desktop\sometexfile.tex", "w", encoding='utf8') as file :
    #     file.writelines("\\documentclass{article}\n")
    #     file.writelines("\\begin{document}\n")
    #     file.writelines("Hello Palo Alto!\n")
    #     file.writelines("\\paragraph{Hello Palo Alto2!}\n")
    #     file.writelines("\\paragraph{Hello Mindenki!}\n")
    #     file.writelines("\\paragraph{Én vagyok Árpi!}\n")
    #     # file.writelines("Kéne valami új szöveg is! :-D !\n")
    #     # file.writelines("\\paragraph{Ez egy új sor!}\n")
    #     for mondat in mondatok:
    #         sor = "\\paragraph{" + mondat + "}\n"
    #         print(sor)
    #         file.write(sor)
    #     file.writelines("\\end{document}\n")
    #
    # x = subprocess.call(r"pdflatex C:\Users\Apu\Desktop\sometexfile.tex -output-directory=C:\Users\Apu\Desktop")
    # if x != 0 :
    #     print("Exit - code    not 0, check    result!")
    # else :
    #     os.system(r"start C:\Users\Apu\Desktop\sometexfile.pdf")
    #     # os.system(r"start C:\Users\Apu\Desktop\Gyerek_new.txt")
    #
    # print(txt)
