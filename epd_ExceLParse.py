# -*- coding: UTF-8 -*-
import datetime
# import sys
import openpyxl
import os
import shutil
from epd_util import Epd_util


# epd_batchinfo
# epd_batchstatement
# epd_pginfo
# epd_expertinfo
# epd_projectinfo
# epd_log


def loadExcelData(filenamepath, outputpath='./'):

    (filename, ext) = os.path.splitext(os.path.basename(filenamepath))

    wb = openpyxl.load_workbook(filenamepath)
    foldname = '%s_%s生成' % (filename,
                            str(datetime.datetime.now().strftime('%Y%m%d')))
    sqlfilenamepath = outputpath + foldname + '/'
    if os.path.exists(sqlfilenamepath):
        shutil.rmtree(sqlfilenamepath)
    os.makedirs(sqlfilenamepath)
    batchid = wb['epd_batchinfo']['A3'].value
    batchgroupid = wb['epd_batchinfo']['F3'].value
    for sheet in wb.sheetnames:
        print('解析表%s开始' % (sheet))
        parseSheetData(wb[sheet], sqlfilenamepath, batchid, batchgroupid)
        print('解析表%s完成' % (sheet))
    pass
    # parseSheetData(wb['epd_pginfo'], sqlfilenamepath, batchid,
    #                batchgroupid)


def parseSheetData(sheet, sqlfilenamepath, batchid, batchgroupid):
    epd_u = Epd_util()
    sheet_title = sheet.title
    columnpart = epd_u.BASE_SQL[sheet_title]
    valuepart = epd_u.VALUE_SQL[sheet_title]
    maxRow = sheet.max_row
    maxCol = sheet.max_column
    outputfilename = sheet_title + '_' + str(
        datetime.datetime.now().strftime('%Y%m%d%H%M')) + '.sql'
    with open(sqlfilenamepath + outputfilename, 'w', encoding='utf-8') as fw:
        for row in sheet.iter_rows(row_offset=2, max_row=maxRow - 2):
            rowlist = []
            for cell in row:
                cellvalue = cell.value
                # if not cellvalue: is None 判断是否None
                if cellvalue is None:
                    rowlist.append('')
                else:
                    rowlist.append(cellvalue)
            if sheet_title == 'epd_batchstatement':
                rowlist.append(batchgroupid)
            if sheet_title == 'epd_pginfo':
                rowlist.append(batchid)
                rowlist.append(batchgroupid)

            mainsql = columnpart + valuepart.format(rowlist)
            fw.write(mainsql + '\n')
        fw.write('--%s数据共计%d条\n\n' % (sheet_title, maxRow - 2))

    pass


if __name__ == "__main__":
    # loadExcelData(sys.argv[1])
    # loadExcelData(
    #     'D:/cvsdocument/应用开发部\科研计划项目\专家评审费发放管理系统/维护文档/2018年度/万达认定数据导入/原始备份/高企财务导数据2016.xlsx',
    #     'D:/cvsdocument/应用开发部/科研计划项目/专家评审费发放管理系统/维护文档/2018年度/万达认定数据导入/导入脚本/')
    loadExcelData(
        'D:/cvsdocument/应用开发部\科研计划项目\专家评审费发放管理系统/维护文档/2018年度/万达认定数据导入/原始备份/高企财务导数据2016.xlsx'
    )
    pass
