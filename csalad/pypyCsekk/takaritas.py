def create_pdf_takaritas(p_datum):

    szoveg = [(0,10,36,"B","Kedves Lakótársak!","C")
              ,(0,20,22,"","A takarítási díjat","L")
              ,(0,30,36,"B","Hétfőn","C")
              ,(0, 40,36,"", "DÁTUM", "C")
              ,(0, 50,36,"", "1900 – 2000", "C")
              ,(0, 60,22,"", "között szedem!", "L")
              ,(0, 70,22,"", "Üdvözlettel:", "C")
              ,(0, 80,22,"", "Losonczi Árpád", "R")

             ]

    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_text_color(0, 0, 0)
  #  pdf.set_font("times", size=18)

    pdf.add_font('Arial', '', r"c:\WINDOWS\Fonts\Times.ttf", True)
    tav = 4
    start = 202
    pos = start

    for item in szoveg:
#        pdf.set_xy(item[0], item[1])
        pdf.set_xy(10, item[1])
        print(item[3],":",item[2])
        pdf.set_font('Arial', "", item[2])
        pdf.cell(0, 0, txt= item[4], markdown=False, align = item[5])
        pdf.char_vpos = "SUP"
        pdf.write(txt="56")

    pdf.add_page()

    pdf.output("./tmp/fajl_takaritas.pdf")
"""
    pdf.cell(5, "Kedves Lakótársak!")
    pdf.cell(10, "A takarítási díjat")
    pdf.cell(15, "Hétfőn")
    pdf.cell(25, "(2022.06.13)")
    pdf.cell(35, "1900 – 2000")
    pdf.cell(45, "között szedem!")
    pdf.cell(55, "Üdvözlettel:")
    pdf.cell(65, "Losonczi Árpád")
"""
