from efficient_apriori import apriori
import pandas as pd
#转化Excel数据为列表
source_data = pd.read_excel('data.xls')
list = source_data.values.tolist()
print(list)
# list = [('低1','中2','高4'),
#         ('低1','低2'),
#         ('高2')]
# print(list)
# list = [['低1','中2','高4'],
#         ['低1','低2'],
#         ['高2']]
# print(list)
#effect_apriori 算法
transactions = list
itemsets, rules = apriori(transactions, min_support=0.4,  min_confidence=1)
print(itemsets)
print(rules)

