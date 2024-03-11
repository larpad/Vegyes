# create_table.py

def create_table(excel_data):
    table_data = []
    
    if excel_data is not None:
        for index, row in excel_data.iterrows():
            table_row = []
            for col in excel_data.columns:
                table_row.append(row[col])
            table_data.append(table_row)
    
    return table_data
