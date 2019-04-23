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




