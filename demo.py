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


#用函数打印斐波那契数列
def fib1(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return 'done1'  

print(fib1(10))

#把fib函数改成generator
'''
一个函数定义中包含yield关键字，
那么这个函数不再是一个普通函数，
而是一个generator
'''
def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done2'

n=fib2(10)
while True:
    try:
        x=next(n)
        print('n:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
    
o=odd()
for i in o:
    print(i)

#python迭代器
#可迭代对象Iterable:可以直接作用于for循环的对象
#使用isinstance()判断一个对象是否为Iterable对象
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance(([]),Iterable))
print(isinstance('abc',Iterable))
print(isinstance(100,Iterable))
print(isinstance(odd(),Iterable))

#迭代器Iterator:可以被next()函数调用并不断返回下一个值的对象
#可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))

#对比一下
print('List and generator:')
print(isinstance([x*x for x in range(10)],Iterator))
print(isinstance((x*x for x in range(10)),Iterator))

print(isinstance(odd(),Iterator))

#把list,dict,str等Iterable变成Iterator可以使用iter()函数
print('iter()强制转换:')
print(isinstance(iter([x*x for x in range(10)]),Iterator))
print(isinstance(iter('abc'),Iterator))

'''
本部分小结：凡是可作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型，它表示一个惰性计算的序列
集合数据类型如list,dict,str等是Iterable但不是Iterator
可以通过iter()函数获得一个Iterator对象
'''

#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for i in [1,2,3,4,5]:
    print(i)
#等价于
it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
    
#tuple是不是Iterator:
print('tuple是不是Iterator？')
print(isinstance((1,2,3,4,5),Iterator))
print('显然不是')

#Python生成器和迭代器这篇就够了
#列表 [0，1，2，3，4，5，6，7，8，9]，要求你把列表里面的每个值加1
L=[x for x in range(10)]
for i in L:
    L[i]+=1
print(L)

#方法二：列表生成式
Lis = [x+1 for x in range(10)]
print(Lis)

'''
为什么用到生成器？
通过列表生成式，我们可以直接创建一个列表，
但是，受到内存限制，列表容量肯定是有限的，
而且创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间，
在Python中，这种一边循环一边计算的机制，称为生成器：generator

python中生成器是迭代器的一种，使用yield返回值函数，
每次调用yield会暂停，
而可以使用next()函数和send()函数恢复生成器。

生成器类似于返回值为数组的一个函数，
这个函数可以接受参数，可以被调用，
但是，不同于一般的函数会一次性返回包括了所有数值的数组，
生成器一次只能产生一个值，这样消耗的内存数量将大大减小，
而且允许调用函数可以很快的处理前几个返回值，
因此生成器看起来像是一个函数，但是表现得却像是迭代器
'''





















