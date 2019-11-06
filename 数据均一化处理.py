print("Author_:运河青檀")
import numpy as np
import pandas as pd
import xlwt
#功能实现：读取Excel表格中的数据，表格数据转化成二维数组，对数组列归一化处理（数组x行y列）
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
#array = array.T                #处理列
minVals = array.min(1)         #找出每一行中的最小值
maxVals = array.max(1)         #找出每一行中的最大值
ranges = maxVals - minVals
normalData = np.zeros(np.shape(array)) #创建一个和array数组相同的以0填充的数组
m = array.shape[1]                      #取出array数组中的列，即y
minVals_array = np.tile(minVals,(m,1))  #创建一个x行y列，数据为x行的minVals数组
ranges_array = np.tile(ranges,(m,1))
minVals_array  = minVals_array .T       #创建最小值数组
ranges_array  = ranges_array.T          #创建极差数组
normalData = (array - minVals_array) / ranges_array
#normalData = normalData.T   #处理列
save(normalData,'normalData.xls')      #存入当前文件夹下

#转载自https://www.cnblogs.com/chulin/p/9721852.html