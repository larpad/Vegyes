import io
import os
import sys

from fpdf import FPDF

class PDF(FPDF):
    pass

pdf = PDF( orientation= 'P', unit= 'mm', format='A4')
pdf.set_author('Losonczi Árpád')
pdf.set_creator('Losonczi Árpád')
pdf.set_subject('Takarítási díj')
pdf.set_title('Takarítási díj')
pdf.set_keywords('lakótársak,takarítás')
pdf.add_page()

# pdf.write('Kedves Lakótársak')
pdf.set_font('Times','B',16)
pdf.cell(0,0,'Kedves Lakótársak!',0,0,'C')

pdf.set_font('Times','',48)
pdf.write(12,'Text\n')
pdf.cell(0,0,'Kedves Lakótársak!',0,0,'C')
pdf.set_font('Times','',48)
pdf.write(84,'Text')
pdf.write(48,'Text','http://goto.to')


pdf.output('test.pdf','F')

os.startfile('test.pdf')


