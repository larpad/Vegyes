from bl_excel import *

import os
from fpdf import *
from pypdf import *
import requests
import json

"""
pdf.set_title("Befizetve")
pdf.set_author("Losonczi Árpád")
pdf.set_creator("Losonczi Árpád as Creator")
pdf.set_subject("Ez a számla is be van fizetve")
pdf.set_keywords("PDF, Python, Tutorial, Számla, GMK")
"""

def crete_watermark(p_tabla):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_fill_color(255,255,0)
    pdf.rect(65, 198, 80, 32, "F")
    pdf.set_font('helvetica', size=12)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("times", size=18,)

    pdf.add_font('Arial', '', r"c:\WINDOWS\Fonts\arial.ttf", True)
    pdf.set_font('Arial', '', 8)
    tav = 4
    start = 202
    pos = start
    for i in [8,5,9,6,4,3,7]:
        item = p_tabla[i]
        pdf.set_xy(65, pos)
        if i != 8:
            text =  item[0] + " : " + item[1]
        else:
            text =  item[1]

        pdf.cell(0, 0, txt= text, markdown=False)
        pdf.cell(0, 0, txt= text)
        pos += tav

    x = 30
    y = 230
    with pdf.local_context(text_mode="STROKE", line_width=3):
        with pdf.rotation(angle=50, x=30, y= 230):
            pdf.set_font('ARIAL', style="B", size=72)

            pdf.set_draw_color(255, 0, 0)
            pdf.text(x=x, y=y, txt="BEFIZETVE")

    pdf.output("fajl_pecset.pdf")
# --------------------------------------------------------
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


# --------------------------------------------------------

def create_pdf_pecsetelt(p_source_path):
    merger = PdfWriter()

    fajl_source = open(p_source_path, "rb")
    pdf_source = PdfReader(fajl_source)
    source_page = pdf_source.pages[0]

    fajl_watermark = open("fajl_pecset.pdf", "rb")
    pdf_watermark = PdfReader(fajl_watermark)
    watermark_page = pdf_watermark.pages[0]

    source_page.merge_page(watermark_page)

    pdf_output = PdfWriter()
    pdf_output.add_page(source_page)

    file_output = open("pecsetelt.pdf", "wb")

    pdf_output.write(file_output)
    file_output.close()
    fajl_watermark.close()
    fajl_source.close()
# --------------------------------------------------------

def pecseteles(p_xls_path,p_pdf_path):


    l_befizetes = get_befizetes(p_xls_path)

    crete_watermark(l_befizetes)
    create_pdf_pecsetelt(p_pdf_path)

    os.remove("fajl_pecset.pdf")
#    os.remove(p_xls_path)
#    os.remove(p_pdf_path)

