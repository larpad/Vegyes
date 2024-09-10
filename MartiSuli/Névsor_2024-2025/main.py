import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm, cm
from loguru import logger
import openpyxl
import subprocess
import platform

def process_excel_and_generate_pdf(input_dir, output_dir, excel_file, pdf_file):
    try:
        logger.info("Starting Excel processing and PDF generation")

        # Read Excel file
        excel_path = os.path.join(input_dir, excel_file)
        try:
            df = pd.read_excel(excel_path, sheet_name='Baksa', engine='openpyxl')
            logger.info(f"Read Excel file: {excel_path}")
        except Exception as e:
            logger.error(f"Error reading Excel file: {str(e)}")
            raise

        # Sort the dataframe by 'Osztály' and 'Sorsz'
        df = df.sort_values(['Osztály', 'Sorsz'])

        # Process data and prepare PDF content
        pdf_path = os.path.join(output_dir, pdf_file)
        try:
            doc = SimpleDocTemplate(
                pdf_path,
                pagesize=A4,
                rightMargin=1*cm, leftMargin=1*cm,
                topMargin=1*cm, bottomMargin=1*cm
            )
            logger.info(f"Created PDF document: {pdf_path}")
        except Exception as e:
            logger.error(f"Error creating PDF document: {str(e)}")
            raise

        story = []
        styles = getSampleStyleSheet()

        # Header style
        header_style = ParagraphStyle(
            'Header',
            parent=styles['Heading1'],
            fontSize=12,
            alignment=1,
        )

        # Table
        try:
            for osztaly, group in df.groupby('Osztály'):
                # Add header for each group
                story.append(Paragraph(f"{osztaly}", header_style))
                
                data = [["", "Oktatási azonosító", "Tanuló neve", "Osztályzat"]]
                for _, row in group.iterrows():
                    data.append([str(row['Sorsz']), row['Oktatási azonosító'], row['Tanuló neve'], ""])

                # Calculate column widths based on content
                sorsz_width = max(len(str(row[0])) for row in data[1:]) * 2.5
                tanulo_neve_width = max(len(str(row[2])) for row in data) * 2.5
                
                # Set minimum widths for each column
                col_widths = [
                    sorsz_width,  # Sorsz
                    40 * mm,  # Oktatási azonosító
                    tanulo_neve_width,  # Tanuló neve
                ]
                
                # Calculate remaining width for the Osztályzat column
                total_width = A4[0] - doc.leftMargin - doc.rightMargin
                remaining_width = total_width - sum(col_widths)
                col_widths.append(remaining_width)  # Osztályzat

                table = Table(data, colWidths=col_widths)
                table.setStyle(TableStyle([
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('ALIGN', (0, 1), (1, -1), 'CENTER'),
                    ('ALIGN', (2, 1), (2, -1), 'LEFT'),
                    ('ALIGN', (3, 1), (3, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),
                    ('FONTSIZE', (0, 0), (-1, -1), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),  # Reduced bottom padding
                    ('TOPPADDING', (0, 0), (-1, -1), 2),  # Added top padding
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('LEADING', (0, 0), (-1, -1), 14)  # Set line height to slightly more than font size
                ]))
                story.append(table)
                story.append(PageBreak())
                logger.info(f"Added table for Osztály: {osztaly} to PDF")

        except Exception as e:
            logger.error(f"Error creating table for PDF: {str(e)}")
            raise

        # Generate PDF
        try:
            doc.build(story)
            logger.info(f"Generated PDF: {pdf_path}")
            logger.success("Finished Excel processing and PDF generation")
        except Exception as e:
            logger.error(f"Error building PDF: {str(e)}")
            raise

        return pdf_path

    except Exception as e:
        logger.error(f"Error during PDF generation: {str(e)}")
        raise

def open_pdf(pdf_path):
    try:
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', pdf_path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(pdf_path)
        else:  # linux variants
            subprocess.call(('xdg-open', pdf_path))
        logger.info(f"Opened PDF: {pdf_path}")
    except Exception as e:
        logger.error(f"Error opening PDF: {str(e)}")

def main():
    try:
        input_dir = r"V:\DEVELOP\DATA\ARANY_BAKSA\2024-2025\Baksa_WORDS"
        output_dir = r"V:\DEVELOP\DATA\ARANY_BAKSA\2024-2025\Baksa_WORDS"
        excel_file = "Baksa.xlsx"
        pdf_file = "Baksa_uj.pdf"

        logger.add("file_{time}.log", level="DEBUG", rotation="1 week")
        logger.info("Program started")

        pdf_path = process_excel_and_generate_pdf(input_dir, output_dir, excel_file, pdf_file)
        open_pdf(pdf_path)
    except Exception as e:
        logger.error(f"An error occurred in main: {str(e)}", exc_info=True)
    finally:
        logger.info("Program finished")

if __name__ == "__main__":
    main()

# A program futtatásához szükséges egy requirements.txt fájl, amely tartalmazza a következő függőségeket:
# pandas
# reportlab
# loguru
# openpyxl
#
# A program meghívása a következő paranccsal történhet:
# python main.py
