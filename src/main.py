import xls_utils as xls_ut
import mysql_utils as mysql_ut


if __name__ == "__main__":
    try:
        table = "media"
        column_names, rows = mysql_ut.fetch_table_data(table)
        export_to_excel = xls_ut.export_to_excel(column_names,
                                                 rows,
                                                 "Migrated medias")
    except Exception as e:
        print(f"Error: {e}")
