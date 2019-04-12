# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:56:41 2019

@author: ASUS 
"""
#默认参数
def endWrong(L=[]):
    L.append("END")
    return L

def endAccepted(L= None):
    if L==None:
        L=[]
    L.append("END")
    return L

print(endWrong([1,2,3]))
print(endAccepted([1,2,3]))
print(endWrong())
print(endWrong())
print(endWrong())
print(endAccepted())
print(endAccepted())
print(endAccepted())

#可变参数
def calc(*number):
    sum=0
    for i in number:
        sum+=i*i
    return sum
print(calc(1,2))
print(calc())
numl=[1,2,3]
numt=(1,2,3)
print(calc(*numl))
print(calc(*numt))

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(1))
print(fact(5))


L=[1,2,3,4,5,6,7,8,9,10]
R=[]
for i in range(0,5,1):
    R.append(L[i])
print(R)
#左闭右开区间
print(L[0:5])
print(L[-3:-1])
print(list(range(0,100,5)))
print((1,2,3,4,5,6,7,8,9,10)[1:3])

'''
字符串可以看成一种list，每个元素就是一个字符。
因此字符串可以用切片操作，只是操作结果仍是字符串。
在许多编程语言中，针对字符串提供了许多各种截取函数（例如substring),
其实目的就是对字符串切片。python没有针对字符串的截取函数，只需要切片
一个操作就可以完成，非常简单。
'''

print('ABCDEFG'[:3])

#dict也可以迭代
d={1:2,3:4,5:6,7:8,9:10,11:12}
for i in d:
    print(i)

for i in d.values():
    print(i)

for k,v in d.items():
    print(k,v)  

for ch in 'ABCDEFG':
    print(ch)
    
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(1234567,Iterable))
print(isinstance(124,int))
print(isinstance("str",int))

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in[(1,1),(2,2),(3,'a')]:
    print(x,y)

print(list(range(55,58)))

#用列表生成式代替循环
L=[]
for i in range(1,11):
    L.append(i*i)
print(L)

L2=[x*x for x in range(1,11)]
print(L2)

L3=[x*x for x in range(1,11) if x%2==0]
print(L3)

#两层循环生成全排列
L4=[m+n for m in 'ABC' for n in 'abc']
print(L4)

L5=[m+n for m in 'ABC' for n in 'abc' if n!='b']
print(L5)

import os #导入os模块
print(d for d in os.listdir('.')) # os.listdir可以列出文件和目录

d={'q':"102",'m':"103",'c':"104"}
for k,v in d.items():
    print(k,"=",v)

c=[k+"="+v for k,v in d.items()]
print(c)


d={'q':102,'m':103,'c':104}
for k,v in d.items():
    print(k,"=",v)

c=[str(k)+"="+str(v) for k,v in d.items()]
print(c)


#把一个list中的所有字符串变成小写
L6=['AsdFgHjkl','QwERTYUiop']
L7=[s.lower() for s in L6]
print(L7)
L8=[s.upper() for s in L6]
print(L8)


#生成器generator和列表生成器辨析
L=[x*x for x in range(10)]
print(L)

#创建L和g的区别仅在于最外层的[]和(),L是一个list,g是一个generator
#我们可以直接打印list的每一个元素
#我们可以通过next()函数获得generator的下一个返回值
'''
generator保存的是算法，每次调用next(g),就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
另外，不断调用next(g)实在是太变态了，
正确的方法是使用for循环，因为generator也是可迭代对象。
'''
g=(x*x for x in range(10))
print(g)
print(next(g))
print("Haha")
for i in g:
    print(i)




















