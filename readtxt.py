# #coding=utf-8
# # # fo = open('aa.txt',encoding = 'UTF-8')
# # # f = fo.read()
# # # print(f)r'E:\22.txt'
# # import io
# # import os
# # print(os.path.abspath(__file__))
# # f = io.open('E:\\22.txt', 'r', encoding='GB2312')
# #
# # print(f.read())
# # f.seek(0,0)
# #
# # print(f.read())
# # print("=========")
import pandas as pd
import os
path = r'G:/chen'
path = os.chdir(path)
path = os.getcwd()
filelist = []
for root,dirs,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.xls':
            filelist.append(file)
print(filelist)
dflist = []
for i in range(len(filelist)):
    dflist.append(pd.read_excel(filelist[i],header = 1,skiprows = 0))
print(dflist)
#data = pd.concat(dflist)  #表格合并
#data.to_excel('data3.xls')
