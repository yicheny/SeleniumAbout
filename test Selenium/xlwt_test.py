import xlwt
from datetime import datetime

def xlwt_test():
    hlHeader = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    formatDMY = xlwt.easyxf(num_format_str='D-MMM-YY ')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('测试结果1')

    ws.write(0, 0, '测试时间', hlHeader)
    # ws.write(1, 0, datetime.now(), formatDMY)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    # ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save('example.xls')