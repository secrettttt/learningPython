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

#排序：sort和sorted
l = [7,8,9,10,1,6,5,3,2,4]
l.sort()
print(l)

l = [7,8,9,10,1,6,5,3,2,4]
l2 = sorted(l)
print(l2)

#切片，步进值为2
print(l[::2])

#当需要对列表或元组进行翻转时，一个很聪明的用法就是向步进传值-1
print(l[::-1])

#遍历一个序列时同时追踪当前元素的索引，下面是一种方法
i=0
for value in l:
    print(i,value)
    i+=1

#Python内建了enumerate函数，返回(i,value)元组的序列
for i,value in enumerate(l):
    print(i,value)



#zip：将列表、元组或其他序列的元素配对
seq1 = [1,2,3,4,5]
seq2 = ('a','b',1,[1,2,3,4],'string')
seq3 = zip(seq1,seq2)
print(seq3)
print(dict(seq3))

seq1 = [1,2,3,4,5]
seq2 = ('a','b',1,[1,2,3,4],'string')
seq3 = zip(seq1,seq2)
print(list(seq3))

#参数不止两个
seq1 = [1,2,3,4,5]
seq2 = ('a','b',1,[1,2,3,4],'string')
seq3 = zip(seq1,seq2)
seq4 = zip(seq1,seq2,seq3)
print(list(seq4))

#zip常用的场景为同时遍历多个序列，有时候会和enumerate同时使用
seq1 = [1,2,3,4,5]
seq2 = ('a','b',1,[1,2,3,4],'string')
#想想为什么for i,[a,b] in enumerate(zip(seq1,seq2))不对？
#和for i,（a,b） in enumerate(zip(seq1,seq2))有什么区别？
for i,[a,b] in enumerate(zip(seq1,seq2)):
    print('{0}: {1},{2}'.format(i,a,b))

'''
行的列表转换成列的列表
'''
#zip机智的用法：把行的列表转换成列的列表
seq = [('a',1),('b',2),('c',3),('d',4),('e',5)]
left,right = zip(*seq)
print(left)
print(right)

#reversed函数将序列的元素倒序排列
#请牢记，reversed是个生成器，因此如果没有实例化(例如使用list函数或进行for循环)的时候，它并不会产生一个倒序的列表
print(reversed(range(10)))
print(list(reversed(range(10))))

#dict
d1 = {'a':'some value','b':[1,2,3,4,5],'c':'an integer'}
print(d1)
d1[7]='hello world'
print(d1)
d1['b']=(1,2)
print(d1)

#检查字典是否含有某个键
print('b' in d1)
d1[5]='some value'
print(d1)
d1['dummy']='another value'
print(d1)
#删除dict中的某个值：可以使用del或pop关键字，pop方法会在删除的同时返回被删除的值，并删除键
del d1[5]
print(d1)

res = d1.pop('dummy')
print(res)
print(d1)

#keys和values方法分别提供字典键、值的迭代器
k = list(d1.keys())
print(k)
v= list(d1.values())
print(v)

d2 = {'z':123,'y':456}
#使用update方法将两个字典合并
d1.update(d2)
print(d1)

#从序列中生成字典
key_list = [1,2,3,4,5]
value_list = [5,4,3,2,1]
mapping = {}
for (key,value) in zip(key_list,value_list):
    mapping[key] = value
print(mapping)

mapping = {}
mapping = dict(zip(range(1,6),reversed(range(1,6))))
print(mapping)

#将列表中的每一个字符串根据首字母分类为包含列表的字典
words = ['apple','bat','bar','atom','book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)

#更好的方法
words = ['apple','bat','bar','atom','book']
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter,[]).append(word)
print(by_letter)

words = ['apple','bat','bar','atom','book']
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)

'''
字典的值可以是任何Python对象，
但是键必须是不可变对象，
例如标量类型（整数、浮点数和字符串）或元组（元组内的对象也必须是不可变对象）。
通过hash函数可以检查一个对象是否可以哈希化（即是否可以用作字典的键）
'''
print(hash('string'))
print(hash((1,2,3,4,5)))
print(hash(tuple([1,2,3,4,5])))

#集合是一种无序且元素唯一的容器，你可以认为集合也像字典，但是只有键没有值
#通过set函数
print(set([2,2,2,2,3,3,1,2,4,5,6,6,5,7,7,8]))
#通过大括号
print({2,2,2,2,2,3,3,1,2,4,5,6,6,5,7,7,8})

#集合操作
a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10,11,12,13,14,15,16}

#并集
print(a|b)
print(a.union(b))

#交集
print(a&b)
print(a.intersection(b))

#给定一个字符串列表，过滤出长度大于2的，并将字母改为大写
sl = ['hello','as','for','in','on','end','start']
SL = []
for s in sl:
    if len(s)>2:
        SL.append(s.upper())
print(SL)

#列表推导式
sl = ['hello','as','for','in','on','end','start']
SL = [s.upper() for s in sl if len(s)>2]
print(SL)

#类似的还有集合推导式、字典推导式

#求包含字符串列表中字符串长度的集合
lenSet = {len(s) for s in sl}
print(lenSet)

#字典推导式示例
dicTemp = {index:value for index,value in enumerate(sl)}
print(dicTemp)

'''
map():根据提供的函数对指定序列做映射。
map(function, iterable, ...)
'''
sl = ['hello','as','for','in','on','end','start']
lenSet = map(len,sl)
print(set(lenSet))

#嵌套列表推导式
all_data = [['John','Emily','Michael','Mary','Steven'],['Maria','Juan','Javier','Natalia','Pilar']]
#获得一个列表包含所有含有2个以上字母e的名字
data_ee = []
for i in all_data:
    for j in i:
        temp = 0
        for k in range(len(j)):
            if j[k] == 'e':
                temp += 1
        if temp >= 2:
            data_ee.append(j)
print(data_ee)        

#列表推导式
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e')>=2]
    names_of_interest.extend(enough_es)
print(names_of_interest)

#嵌套列表推导式
result =  [name for names in all_data for name in names if name.count('e')>=2]
'''
理解：
result =  [name for names in all_data 
                    for name in names 
                        if name.count('e')>=2]
'''
print(result)

#将含有整数元组的列表扁平化为一个简单的整数列表
some_tuples = [(1,2,3),(4,5,6),(7,8,9)]
flattened = [data for tuple_data in some_tuples for data in tuple_data]
print(flattened)

#嵌套列表表达式：嵌套for循环可以转换成嵌套列表表达式
#请牢记：for表达式的顺序应当和你写嵌套for循环来替代列表推导式的顺序一致
flattened = []
for tuple_data in some_tuples:
    for data in tuple_data:
        flattened.append(data)
print(flattened)

#可以嵌套多层列表推导式，但是超过两到三层之后就要开始考虑这样做是否有利于代码可读性了

#Python的函数是对象

#匿名(Lambda)函数
f = lambda x: (x**2)*3.14
print(f(2))
print(f(3))

def apply_to_list (some_list,f):
    return [f(x) for x in some_list]
init = list(range(10))
print(apply_to_list(init,lambda x : x*2))

#根据字符串中不同字母的数量对一个字符串集合进行排序
strings = ['foo','card','bar','aaaa','abad']
strings.sort(key = lambda x:len(set(list(x))))
print(strings)

#函数柯里化：一个函数有多个参数，固定部分参数的值后衍生出新的函数。

'''
生成器：
迭代器：
'''

#错误和异常处理
#如果float(x)执行时抛出了异常，则代码段中的except部分代码将会被执行
def attempt_float_01(x):
    try:
        return float(x)
    except:
        return x

print(attempt_float_01('1.2345'))

def attempt_float_02(x):
    try:
        return float(x)
    except ValueError:
        return x

print(attempt_float_02('somthing'))

#可以通过多个异常类型写成元组形式同时捕获多个异常（小括号是必不可少的）
def attempt_float_03(x):
    try:
        return float(x)
    except (ValueError,TypeError):
        return x

print(attempt_float_03((1,2,3)))

#某些情况下，希望一部分代码无论try代码块是否报错都要执行，为了实现这个目的，使用finally关键字
f = open('None.txt','w') 
try:
    pass
except:
    print('Failed')#try代码块抛出异常时执行
else:
    print('Succeeded')#try代码块成功执行时，才会执行
finally:#无论哪种情况，总会执行
    f.close()
    





