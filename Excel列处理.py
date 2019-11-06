import numpy as np
import pandas as pd
import xlwt
db=['bridge','bus','bus station ','highway','subway','taxi','train']
dflist = pd.read_excel('data.xls')
count = 0
aflist =[]
for i in db:
    count+=1
    k1 = list(dflist[i].values)
    print(k1)
    for j in k1:
        if j == '高':
            j = '高' + str(count)
            j= ''.join(j)
            aflist.append(j)
        elif j == '中':
            j = '中' + str(count)
            aflist.append(j)
        elif j == '低':
            j = '低' + str(count)
            aflist.append(j)
        elif j == '':
            j = ''
            aflist.append(j)

print(aflist)
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
data_write('dflist.xls',aflist)

