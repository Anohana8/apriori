# import numpy as np
# import pandas as pd
# num = np.array([[0,0,9,0],[9,3,1,0],[0,0,0,0]])
# list_rows_mean=np.mean(num,axis=0)
# list_cols_mean=np.mean(num,axis=0)
# list_rows_std=np.std(num,axis=1)
# list_rows_std=np.std(num,axis=1)
#
#
# def means_std_rows(a1, l1, l2):
#
#     return x, y
#
#
# def means_std_cols(a2, l3, l4):
#     return x, y
#
#
# [rows, cols] = num.shape
# print(rows, cols)
# count=0
# for i in range(rows):
#     (mean1,std1) = means_std_rows(count,list_rows_mean,list_cols_mean)
#     for j in range(cols):
#         x=num[i, j]
#         x = round((x - mean1) /std1, 2)
#         print(x,ens=',')
#     coun=count+1
#     print()
#行列单行均一化
import numpy as np
import pandas as pd
db=['bridge','bus','bus station ','highway','subway','taxi','train']
dflist = pd.read_excel('data.xls')
# k0 = dflist.ix[10].values
# arr = np.asarray(k0)
# for x in k0:
#     x = round((x - np.min(arr)) / (np.max(arr) - np.min(arr)), 2)
#     print("读取指定行的数据：{0}".format(x))
# print()
# print('===============================')
list1=[]
for i in db:
    k1 = list(dflist[i].values)
    arr = np.asarray(k1)
    for x in k1:
        x = round((x - np.min(arr)) / (np.max(arr) - np.min(arr)), 2)
        list1.append(x)
    print()
