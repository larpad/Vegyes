from  datetime import datetime
from PyPDF2 import *
from fpdf import *
# --------------------------------------------------------
"""
pdf.set_title("Befizetve")
pdf.set_author("Losonczi Árpád")
pdf.set_creator("Losonczi Árpád as Creator")
pdf.set_subject("Ez a számla is be van fizetve")
pdf.set_keywords("PDF, Python, Tutorial, Számla, GMK")
"""
# --------------------------------------------------------

def crete_watermark(pExcel):
    p_tabla = [ pExcel.InditoSzamlaszam
               ,pExcel.TranzakciAzonosito
               ,pExcel.RogzitesDatuma
               ,pExcel.TranzakcioAllapota
               ,pExcel.TranzakcioMegnevezese
               ,pExcel.EllenoldaliSzamlaszam
               ,pExcel.Osszeg
               ,pExcel.Kozlemeny
               ,pExcel.KedvezmenyezettNeve
              ]
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_fill_color(255,255,0)
    pdf.rect(65, 198, 80, 32, "F")
    pdf.set_font('helvetica', size=12)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("times", size=18,)

 #   pdf.add_font('Arial', '', r"c:\WINDOWS\Fonts\arial.ttf", True)
 #   pdf.set_font('Arial', '', 8)
    tav = 4
    start = 202
    pos = start
    print(p_tabla);
    for i in [8,5,8,6,4,3,7]:
        item = p_tabla[i]
        pdf.set_xy(65, pos)

        text =  item
        print(item)
        pdf.cell(0, 0, txt= text, markdown=False)
        pos += tav

    x = 30
    y = 230
    with pdf.local_context(text_mode="STROKE", line_width=3):
        with pdf.rotation(angle=50, x=30, y= 230):
#            pdf.set_font('ARIAL', style="B", size=72)

            pdf.set_draw_color(255, 0, 0)
            pdf.text(x=x, y=y, txt="BEFIZETVE")

    pdf.output("fajl_pecset.pdf")
# --------------------------------------------------------
def create_pdf_szoveg(p_szoveg):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_text_color(0, 0, 0)
    pdf.add_font('Font', '', r"c:\WINDOWS\Fonts\Times.ttf", True)
    pdf.add_page()
    StartX = 10
    StartY = 40
    tav = 4
    start = 202
    pos = start

    for item in p_szoveg:
        pdf.set_xy(StartX + item[0], StartY + item[1])
        pdf.set_font('Font', "", item[2])
        l_text = item[4]
        #    pdf.char_vpos = "SUP"
        pdf.cell(0, 0, txt=item[4], markdown=False, align=item[5])

    pdf.add_page()
    pdf.output("./tmp/fajl_takaritas.pdf")

def get_het_napja(p_datum):
    napok = [ "Hétfőn"
             ,"Kedden"
             ,"Szerdán"
             ,"Csütörtökön"
             ,"Pénteken"
            ]
    weekday = datetime.strptime(p_datum, '%Y-%m-%d').date().weekday()
    return napok[weekday].upper()

def create_pdf_takaritas(p_datum):
    szoveg = [ [0,00,36,"B","Kedves Lakótársak!","C"]
              ,[10,40,22,"","A takarítási díjat","L"]
              ,[0,60,40,"B","NAP","C"]
              ,[0,72,28,"B", "DÁTUM", "C"]
              ,[0,90,40,"B", "19:00 – 20:00", "C"]
              ,[10,110,22,"","között szedem!", "L"]
              ,[0,140,22,"", "Üdvözlettel:", "C"]
              ,[50,170,22,"","Losonczi Árpád", "C"]
             ]
    for item in szoveg:
        if item[4] == "DÁTUM":
            item[4] = p_datum.replace("-", ".")
        elif item[4] == "NAP":
            item[4] = get_het_napja(p_datum)

    create_pdf_szoveg(szoveg)

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