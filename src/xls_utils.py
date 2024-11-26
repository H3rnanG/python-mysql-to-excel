import os
import openpyxl


def export_to_excel(column_names, rows, title: str):
    data_path = os.path.join(os.path.abspath("."), "data", "output.xlsx")
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = title
        sheet.append(column_names)
        for row in rows:
            sheet.append(row)
        workbook.save(data_path)
    except Exception as e:
        print(f"Error al exportar el Excel: {e}")
