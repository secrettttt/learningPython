# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:18:58 2019

@author: ASUS
"""

#鸭子类型
from collections import Iterable
a=(1,2,3,4,5)
if not isinstance(a,list) and isinstance(a,Iterable):
    a=list(a)
print(a)

#导入模块

##方法一
#import diyModule
#print(diyModule.PI)

##方法二
#from diyModule import PI,output_number,output_sum
#print(PI)
#print(output_number(100))
#print(output_sum(1,1))

#方法三
import diyModule as dm
print(dm.PI)
print(dm.output_number(3.14))
print(dm.output_sum(12,13))

a = [1,2,3]
b = a
c = list(a)
#is:检查两个引用是否指向同一对象
print(a is b)
#is not:检查两个引用指向的不是相同对象
print(a is not c)
#注意：list函数总是创建一个新的Python列表(即一份拷贝)，我们可以确定c与a是不同的。

# is 和 == 是不同的
print("a is c:",a is c)
print("a == c:",a == c)

#看一个例子
l1=[5,6,7]
l2=[5,6,7]
print("l1 is l2:",l1 is l2)
print("l1 == l2",l1 == l2)

#is和 is not:常用于检查一个变量是否为None
l3 = None
print("l3 is None:",l3 is None)

#a除以b和a整除以b
print("10/3=",10/3)
print("10//3=",10//3)

#count方法计算字符串c的回车符:c.count('\n')
c = '''
abc
def
'''
print(c.count('\n'))

#Python的字符串是不可修改的
a = 'this is a string'
b = a.replace('string','longer string')
print(a)
print(b)

s = 'Python'
print(list(s))

#切片:
#例如：L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(s[:1])
print(s[:2])
print(s[:3])
print(s[2:7])

#原生字符
print("abc\\\\\def\\\ghij\\k")
print(r"abc\\\\\def\\\ghij\\k")

#字符串格式化
template = '{0:.2f} {1:s} are worth US${2:d}'
print(template.format(0.28333,'hello',125))

#python的格式化输出
print("%d"%2)
print("%d %.2f"%(2,3.1415926))
print("%d %.2f %s"%(2,3.1415926,'hello,world'))

#元组拆包
tup = (4,5,6)
a,b,c = tup
print(a)
print(b)
print(c)

#即使是嵌套元组也可以拆包
tup = (4,5,(6,7))
a,b,(c,d) = tup
print(d)

#使用这个功能可以轻易的交换变量名
#在其他语言中，代码可能如下
a = 5
b = 3
print(a,b)
temp = a
a = b
b = temp
print(a,b)

#在Python中交换可以如下完成
a = 5
b = 3
print(a,b)
a,b = b,a
print(a,b)

#拆包的一个常用场景就是遍历元组或列表组成的序列
seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print(a,b,c)
    
for a,b,c in seq:
    print('a={0},b={1},c={2}'.format(a,b,c))


#元组方法：一个常用的方法是count(列表中也可用)，用于计量某个数值在元组中出现的次数
tup = (1,2,3,4,5,6,7,8,9,10,2,2,2,3,4,5,6,7,8,9,10,2)
print(tup.count(2))

l = [1,2,3,4,5,6,7,8,9,10,1,1,1,2,2,3,3,4,4,5,5,6,6]
print(l.count(1))

s = '''
abcdef
ghijk
lmn

'''
print(s.count('\n'))

gen = range(10)
print(gen)
print(list(gen))

#连接和联合列表
l1 = [1,2,None]
l2 = ['a',3,(4,5)]

#连接：代价高，连接过程需要创建新列表并且还要复制对象
print(l1+l2)
#联合：使用extend将元素添加到已经存在的列表是更好的方式
l3 = l1.extend(l2)
print(l1)
print(l3)#理解extend和连接的区别



















































