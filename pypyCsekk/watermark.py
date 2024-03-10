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
        pos += tav

    x = 30
    y = 230
    with pdf.local_context(text_mode="STROKE", line_width=3):
        with pdf.rotation(angle=50, x=30, y= 230):
            pdf.set_font('ARIAL', style="B", size=72)

            pdf.set_draw_color(255, 0, 0)
            pdf.text(x=x, y=y, txt="BEFIZETVE")

    pdf.output("fajl_pecset.pdf")