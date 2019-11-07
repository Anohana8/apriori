
import numpy as np
import pandas as pd
import xlwt


# def save(data,path):
#     f = xlwt.Workbook() #创建工作簿
#     sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
#
#     for i in range(data.shape[0]):
#         for j in range(data.shape[1]):
#             sheet1.write(i,j,data[i,j])
#     f.save(path)


array1 = pd.read_excel('212.xls',sheet_name='Sheet1')
array2 = pd.read_excel('212.xls',sheet_name='Sheet2')
array3 = pd.read_excel('212.xls',sheet_name='Sheet3')
array4 = pd.read_excel('212.xls',sheet_name='Sheet4')
array5 = pd.read_excel('212.xls',sheet_name='Sheet5')
array6 = pd.read_excel('212.xls',sheet_name='Sheet6')
array7 = pd.read_excel('212.xls',sheet_name='Sheet7')
array8 = pd.read_excel('212.xls',sheet_name='Sheet8')
array9 = pd.read_excel('212.xls',sheet_name='Sheet9')

array1 = np.array(array1)
array2 = np.array(array2)
array3 = np.array(array3)
array4 = np.array(array4)
array5 = np.array(array5)
array6 = np.array(array6)
array7 = np.array(array7)
array8 = np.array(array8)
array9 = np.array(array9)


array = array1 + array2 + array3 + array4 + array5 + array6 + array7 + array8 + array9
print(array.shape[0])


# save(array, 'array10.xls')