# import pandas as pd
# import os
# path = r'G:/py'
# path = os.chdir(path)
# path = os.getcwd()
# filelist = []
# for root,dirs,files in os.walk(path):
#     for file in files:
#         if os.path.splitext(file)[1] == '.xls':
#             filelist.append(file)
# print(filelist)
# dflist = []
# for i in range(len(filelist)):
#     dflist.append(pd.read_excel(filelist[i],skiprows = 0))
# print(dflist)
# #data = pd.concat(dflist)  #表格合并
# #data.to_excel('data3.xls')

# import numpy as np
# outp = []
# arr = np.asarray([1,2,3,4,0])
# print(arr)
# # for x in range(len(arr)):
# #     x = (x - arr.mean())/arr.std()
# #     outp.append(x)
# #     i = i+1
# # print(outp)
# import numpy as np
# # arr = np.array(
# # [0   0    0    0    0    0    0   0
# # 1   0    0    0    1    0    0  11
# # 2   8   36    4    2    0    1   4
# # 3   0    1    1    2    0    0   0
# # 4   0    0    0    0    0    0   0
# # 5  18   12    5    3    0    0  36
# # 6   8    2    7    1    0    0   0
# # 7   1    0    0    0    0    0   0
# # 8   0    0    0    0    0    0   0])
# import pandas as pd
# import numpy as np
# dflist = []
# print(dflist)
# dflist = pd.read_excel('data.xls')
# print(dflist)
# print(type(dflist))
# print(dflist.ix[[1,2]].values)
# k1 = list(dflist['train'].values)
# k1 = np.asarray(k1)
# mean1 = k1.mean()
# std1 = k1.std()
# for x in k1:
#     x = round((x - mean1)/std1,2)
#     print(x)
# import numpy as np
#
# arr = np.asarray([0,0,0,0,0,0,6])
# for x in arr:
#     x = round((x - np.min(arr)) / (np.max(arr) - np.min(arr)),2)
#     print(x,end=',')

