# create_pdf.py

from fpdf import FPDF

def create_pdf(table_data, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for row in table_data:
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln()

    pdf.output(output_file)

