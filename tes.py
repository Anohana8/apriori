#'hello,world'
#print('hello,%s' % input('xingming:'))
#print('age=%s,gender=%s' % (input(),input()))
'''a='hello,{0}，成绩提高了{1:.1f}%'
print(a.format('xiaoming',12.4565))
'''
'''a=('a','b')
print(len(a))
b=['a','b']
print(len(b))
print(b[0])
'''
'''list1 = ['a','s','d']
j=0
k=0
for i in list1:
    print(list1[j])
    j+=1
while k<len(list1):
    print(list1[k])
    k+=1
list2 = ['a','b',list1,'c']
#print(list2[2],list2[1][0])
list2.append('dfgf')
list2.insert(1,'lihua')
list2.pop(4)
list2[0] = 'xiaoli'
print(list2,list2[-1])
'''
'''x=(5,6)
list = ['a',5,x]
print(list)
tuple = (2,'r',x)
'''
'''sum=0
print(range(5))
for i in range(5):
    sum+=i
print(sum)
'''
'''n=0
while n<100:     #打印-100的偶数
    n+=1
    if n%2 != 0:
        continue
    print(n,end=' ')
'''
#failure
# map1 = [['marry',65],['kate',70],['davie',99]]
#for i in map1:
#   if map1[i]=='davie':
#        print(map1[i])
'''d = {'marry':65,'kate':70,'davie':90}
d.pop('kate')
print(d['marry'])
a = 'lihua' in d
b = d.get('lili',-1)
print(a,b)
key = ('marry','davie') #增加dict中key数目
d[key] = 57,98
print(d['marry'])
print(d)
'''
'''s = set((1,2,3))
s.add(9)
print(s)

x = set([2,'1',3])
x.remove(3)
print(x)
print(s&x,',and,',s|x)
y = set(tuple())
print(y)
b = 'adb'
b.replace('a','c')
print(b)
'''
'''list1 = {(1,2,3)}
print(list1)
#list2 = {(1,[2,3])}
list3 = set((1,2,3))
print(list3)
#list4 = set((1,[2,3]))
'''
'''array = [[1,3],[3,4],[3,5]]
list1 = []
for i in array:
    list1.extend(list(range(i[0],i[1]+1)))
'''
'''def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('typeerror')
    elif x >= 0:
        return x
    else:
        return -x
print(my_abs('str'))
'''
'''
#位置参数
import math
def move(x,y,step,angle):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny
a = move(2,4,2,math.pi/6)
print(a)
x,y =a
print(x,y)

import math
def move(num1):
    nx = num1[0] + num1[2]*math.cos(num1[3])
    ny = num1[1] + num1[2]*math.sin(num1[3])
    return nx,ny
a = move([2,4,2,math.pi/6])
print(a)
x,y =a
print(x,y)

'''
#默认参数
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('end')
#     return L
# print(add_end(['1','2']))
# print(add_end())
# print(add_end())
# list([1,2,3])
# def cacl(num):
#     sum = 0
#     for n in num:
#         sum = sum + n*n
#     return sum
# print(cacl([1,2,3]))
'''
#可变参数
def cacl(*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum
num = list(input())
num = list(map(int,num))
print(cacl(*num))
'''

# #关键字参数
# other = {'job':'farmer','city':'shanghai','address':'nantong'}
# def person(name,age,**kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     kw['city'] = 'zaozhuang'
#     print('name:',name,',age:',age,',extra:',kw)
# person('davia',21,**other)
# person('lihua',25,city='chongqing')
# print(other)
#
# #命名关键字参数（必须传入参数名）
# def person(name,age,*,city='shanghai',job):
#     print(name,age,city,job)
# person('li',32,job='engineer')
# def person1(name1,age1,*argue,city1='beijing',job1='doctor'):
#     print(name1,age1,argue,city1,job1)
# person1('chen',23,[12,34],'jinan','teacher')
# #*args,**kw表示函数
# def f1(a,b,c=0,*args,d,**kw):
#     print(a,b,c,d,kw)
# args = (1,2)
# kw = {'d':56,'area':'first'}
# f1(*args,**kw)
'''def div(dividend,divisor):
    res = True if dividend * divisor > 0 else False
    dividend = abs(dividend)
    divisor = abs(divisor)
    x=0
    while divisor <= dividend:
        tem_divisor,count=divisor,1
        while tem_divisor <= dividend:
            x+=count
            dividend-=tem_divisor
            tem_divisor<<=1
            count<<=1
    res= min(max(-2**31,x),2**31-1) if res == True else min(max(-2**31,-x),2**31-1)
    return res
'''
# def fact(n):
#     return fact_ite(n,1)
# def fact_ite(num,i):
#     if num==1:
#         return i
#     return fact_ite(num-1,num*i)
# a=fact(int(input()))
# print(a)
# L = list(range(100))
# L1 = L[-6:-1:3]
# print(L1)
# print((2,3,4,5,6,7,7)[::2])
# print('asfdgttfd'[:2])
# d = {'q':3,'t':5,'i':7}
# for i in d:
#     print(i)
# for j in d.values():
#     print(j)
# f=[]
# for k,v in d.items():
#     f.append(k)
# print(f[0])
# print(f)
# from collections import Iterable
# print(isinstance(123,Iterable))
# list1 = ['a','d','g','g']
# for i ,j in enumerate(list1):
#     print(i,j)
# A=[x*x for x in range(1,11) if x%2 != 0]
# print(A)
# print([m+n for m in 'azx' for n in 'yui'])
# import os
# print([d for d in os.listdir('.')])
# d = {'a':1,'b':3,'j':4}
# d=[key + '=' + str(value) for key,value in d.items()]
# print(d)
# s=['AS','DF','FGTR']
# j=['sd','dgfhg','jkll']
# print([i.lower() for i in s])
g = (x*x for x in range(10))
for i in g:
    print(i)
#定义一个斐波那契数
def fib(max):
    b,a,n=1,0,0
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
f = fib(6)
print(f)