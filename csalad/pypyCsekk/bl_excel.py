
import xlrd

def get_befizetes(p_xls_path):
    data = xlrd.open_workbook_xls(p_xls_path)
    sx = []
    sx.append(['sheet_name', data.sheet_by_index(0).name])
    sheet = data.sheet_by_index(0)
    j = 1
    for i in range(4, 13): # Utalás
#    for i in range(5, 10): # Zsebpénz

        key = str(sheet.cell(i, 3).value)
        value = str(str(sheet.cell(i, 7).value))

        sx.append([key, value])
    j += 1

    return sx
