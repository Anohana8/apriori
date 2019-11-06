import pandas as pd
import xlwt
source_data = pd.read_excel('123.xls')
list = source_data.values.tolist()
print(len(list))
dflist = []
for i in list:
    if (i[0] == 0):
        dflist.append('')
    elif (i[0] > 0) and (i[0] <= 0.2143):
        dflist.append('低')
    elif (i[0] >= 0.2222) and (i[0] <= 0.6857):
        dflist.append('中')
    elif (i[0] > 0.6857) and (i[0] <= 1):
        dflist.append('高')


#  将数据写入新文件
def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1

    f.save(file_path)  # 保存文件
data_write('dflist.xls',dflist)


