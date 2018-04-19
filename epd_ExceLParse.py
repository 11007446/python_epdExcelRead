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
    sheetnames = wb.get_sheet_names()
    for sheet in sheetnames:
        parseSheetData(wb.get_sheet_by_name(sheet))
    pass


# epd_batchinfo
# ('','',,'','','',,,,,'ZJ','010',getdate(),'',' 23:59:59' );
# epd_batchstatement
# (newid(),'','','','','','','','',,,,,'','','','','','','','','');
# epd_pginfo
# ('','','','','','',,,,'','',,getdate(),'0','1');
# epd_expertinfo
# ('','','_','','',getdate());
# epd_projectinfo
# ('','','',,getdate());
# epd_log
# ('','',getdate(),'','');


def parseRow(row, sheet_title):
    pass


def parseSheetData(sheet):
    epd_u = Epd_util()
    sheet_title = sheet.title
    sqlpart = epd_u.BASE_SQL[sheet_title]
    maxRow = sheet.get_highest_row()
    maxCol = sheet.get_highest_column()
    for rowIndex in range(2, maxRow):
        rowlist = []
        for colIndex in range(1, maxCol):
            cellvalue = sheet.cell(row=4, column=2).value
            rowlist.append(cellvalue)

    pass


# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# for row in sheet.iter_rows():
#     for cell in row:
#         print(cell.coordinate, cell.value)
# print('--- END OF ROW ---')
if __name__ == "__main__":
    pass
