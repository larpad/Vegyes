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