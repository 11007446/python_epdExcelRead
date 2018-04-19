import openpyxl
from epd_util import Epd_util

# epd_batchinfo
# epd_batchstatement
# epd_pginfo
# epd_expertinfo
# epd_projectinfo
# epd_log


def loadExcelData(filepath):
    wb = openpyxl.load_workbook(filepath)
    for sheet in wb:
        parseSheetData(sheet)
    pass


def parseSheetData(sheet):
    epd_u = Epd_util()
    sheet_title = sheet.title
    sqlpart = epd_u.BASE_SQL[sheet_title]
    pass


# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# for row in sheet.iter_rows():
#     for cell in row:
#         print(cell.coordinate, cell.value)
# print('--- END OF ROW ---')
