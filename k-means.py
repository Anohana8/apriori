print("Author_:运河青檀")
import numpy as np
import pandas as pd
import xlwt
#功能实现：读取Excel表格中的数据（Excel第一行需加列名），表格数据转化成二维数组，对数组每行按比例缩放（数组x行y列）
def save(data,path):
    f = xlwt.Workbook() #创建工作簿
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    [cols,rows] = data.shape
    for i in range(cols):
        for j in range(rows):
            sheet1.write(i,j,data[i,j])
    f.save(path)

array = pd.read_excel('data.xls')  #从当前文件夹下读取
array = np.array(array)
array = array.T  #处理列
sum_rows = array.sum(axis=1)                        #输出每一行求和的列表
sum_rows = sum_rows.T
normalData = np.zeros(np.shape(array)) #创建一个和array数组相同的以0填充的数组
m = array.shape[1]                      #取出array数组中的列，即y
sum_array = np.tile(sum_rows,(m,1))  #创建一个x行y列，数据为x行的sum_rows数组
sum_array  = sum_array.T
normalData = array / sum_array
normalData = normalData.T     #处理列
save(normalData,'normalData.xls')      #存入当前文件夹下
