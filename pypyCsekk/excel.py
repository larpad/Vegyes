def get_befizetes(data):
    sx = []
    sx.append(['sheet_name', data.sheet_by_index(0).name])
    sheet = data.sheet_by_index(0)
    j = 1
    for i in range(4, 13):
        key = str(sheet.cell(i,3).value) # cell_value(i, 3) #.encode('utf-8').decode('utf-8')
        value = str(sheet.cell(i, 7).value) #.encode('utf-8').decode('utf-8')
        sx.append([key,value])
        j += 1

    return sx