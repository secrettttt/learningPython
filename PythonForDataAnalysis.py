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
    

#Python处理文件的基础知识
path = 'file1.txt' #可以用相对路径或绝对路径，这里使用相对路径
f = open(path)#默认情况下，文件以只读模式‘r’打开
print(f.tell())#tell方法给出句柄当前位置

#我们可以像处理列表一下处理文件f,并遍历f中的行内容
temp = []
for line in f:
    temp.append(line)

print(f.tell())#tell方法给出句柄当前位置
print(temp)

f.seek(5)#将句柄的位置改变到文件特定的字节
print(f.tell())

#将文件中的内容形成不带EOL（行结尾标识）的列表
#Python rstrip():删除 string 字符串末尾的指定字符（默认为空格）.
lines = [x.rstrip() for x in open(path)]
print(lines)

#当使用open创建文件对象时，在结束操作时显式地关闭文件是非常重要的
#关闭文件会将资源释放回操作系统
f.close()

#另一种更简单的关闭文件的方法就是使用with语句
with open(path) as f:
    lines = [x.rstrip() for x in f]
print(lines)
#使用with语句文件会在with代码块结束后自动关闭

#将file1.txt的内容写入文件，并且将空行处理掉
with open('file2.txt','w') as handle:
    handle.writelines(x for x in open(path) if len(x)>1)
with open('file2.txt') as f:
    lines = f.readlines()
print(lines)

#NumPy ndarray：多维数组对象
#导入NumPy
import numpy as np

#生成随机数组
data = np.random.randn(2,3)
print(data)
print(data*10)
print(data+data)

#注意：一个ndarray是一个通用的多维同类数据容器，它包含的每一个元素均为相同类型。
#数组的shape属性和dtype属性
print(data.shape)
print(data.dtype)

#通常，”数组“，”NumPy数组“或”ndarray“都表示同一个对象：ndarray对象

#生成ndarray
data = [[1,2,3,4],[5,6,7,8]]
arr = np.array(data)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

#生成一个N*N特征矩阵（对角线位置都是1，其余位置都是0）
#np.identity()和np.eye()的区别在于:np.identity()只能创建方阵
arr = np.identity(3)
print(arr)
arr2 = np.eye(3,4)
print(arr2)

#使用astype方法显式地转换数组的数据类型
arr3 = np.array([1,2,3,4,5])
print(arr3.dtype)
float_arr3 = arr3.astype(np.float64)
print(float_arr3)
print(float_arr3.dtype)

#把浮点数转换成整数，小数点后的部分将会被消除
arr4 = np.array([0.123,1.345,2.567,3.789,4.910])
print(arr4.dtype)
int_arr4 = arr4.astype(np.int64)
print(int_arr4)
print(int_arr4.dtype)

#对于表达数字含义的字符串，也可以用astype将字符串转换成数字
numeric_strings = np.array(['1.234','5.678','9'])
print(numeric_strings.dtype)
numbers = numeric_strings.astype(np.float64)
print(numbers.dtype)
print(numbers)


#NumPy数组算数
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr*arr)
print(arr-arr)
print(1/arr)
print(arr**0.5)
arr2 = np.array([[1,4,5],[2,3,6]])
#同尺寸数组之间的比较，会产生一个布尔型数组
print(arr2>arr)

#基础索引与切片
#一维数组比较简单，和Python的列表很类似
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])

'''
区别于Python的内建列表，数组的切片是原数组的视图。
这意味着数据并不是被复制的，任何对于视图的修改都会反映到原数组上.
'''
arr[5:8]=12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)

#当我改变arr_slice时，变化也会体现在原数组上
arr_slice[0]=99
print(arr)

#不写切片值的[:]将会引用数组的所有值
arr_slice[:]=99
print(arr)


#如果想要一份数组切片的拷贝而不是一份视图的话，必须显式地复制这个数组
arr = np.arange(10)
arr[5:8]=12
print(arr)

arr_copy = arr[5:8].copy()
print(arr_copy)

arr_copy[0] = 99
print(arr)

arr_copy[:] = 99
print(arr)

#和列表进行对比
l = list(range(10))
print(l)
l_slice = l[5:8]
print(l_slice)

l_slice[0] = 12
print(l_slice)
print(l)

#二维数组，每个索引值对应的元素不再是一个值，而是一个一维数组
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[2])

#获得单个元素
print(arr2d[0][2])
#可以通过传递一个索引的逗号分隔列表去选择单个元素
print(arr2d[0,2])
#以上两种方式效果一样

#这是一个2*2*3的多维数组
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)

#arr3d[0]是一个2*3的二维数组
print(arr3d[0])

old_value = arr3d[0]
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_value
print(arr3d)

#类似的arr3d[1,0]返回的是一个一维数组
print(arr3d[1,0])

#需要注意的是，以上的数组子集选择中，返回的都是视图

#一维数组的切片
print(arr)
print(arr[1:6])

#二维数组的切片
print(arr2d)

#选择arr2d的前两“行”
print(arr2d[:2])

#选择arr2d的前两行的后两列
print(arr2d[:2,1:])

'''
可以将索引和切片混合
因为索引和切片的本质都是视图（理解这句话）
例如，我们可以选择第二行但是只选择前两列
'''
print(arr2d[1,:2])

#同样，我们可以选择第三列，但是只选择前两行
print(arr2d[:2,2])

#单独一个冒号表示整个轴上的数组
print(arr2d[:,:1])

#对切片表达式赋值，整个切片都会重新赋值
arr2d[:2,1:] = 0
print(arr2d)

#理解它们的不同
print(arr2d[1,:2])#shape(2,)，意思是一个一维数组，数组中有2个元素
print(arr2d[1:2,:2])#shape(1,2)，意思是一个二维数组，有1行，每行2个元素

#理解它们的不同
print(arr2d[2])#shape(3,)，意思是一个一维数组，数组中有3个元素
print(arr2d[2,:])#shape(3,)，意思是一个一维数组，数组中有3个元素
print(arr2d[2:,:])#shape(1,3)，意思是一个二维数组，有1行，每行3个元素

#布尔索引
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print(names)

#numpy.random的randn函数可以生成一些随机正态分布数据
data = np.random.randn(7,4)
print(data)

#假设每个人名和data数组中的一行相对应，并且我们想选中所有‘Bob’对应的行

#产生一个布尔值数组
print(names == 'Bob')

print('data[names == \'Bob\']:\n',data[names == 'Bob'])

print('data[names == \'Bob\',2:]:\n',data[names == 'Bob',2:])

print('data[names == \'Bob\',3]:\n',data[names == 'Bob',3])

print(names != 'Bob')
print(~(names == 'Bob'))

print(data[~(names == 'Bob')])

#~符号可以在你想要对一个通用条件进行取反时使用
cond = names == 'Bob'
print(data[~cond])

#使用 & 和 |
mask = (names == 'Bob')|(names == 'Joe')
print(mask)
print(data[mask])

#使用布尔值索引选择数据时，总是生成数据的拷贝，即使返回的数组并没有任何的变化

#Python的关键字 and 和 or 对布尔值数组并没有用，请使用 & 和 | 代替。

#把data中的所有负值设置为0
print(data)
data [data < 0] = 0
print(data)

#利用一维布尔值数组对每一行设置数值也是非常简单的
data [names == 'Bob'] = 7
print(data)

#神奇索引
arr = np.empty((8,4))
print(arr)

for i in range(8):
    arr[i] = i

print(arr)

#为了选出一个符合特定顺序的子集，可以通过传递一个包含指明所需顺序的列表或数组来完成
arr2 = arr[[4,3,0,6]]

print(arr)
print(arr2)

#如果是负的索引，将从尾部进行选择
arr3 = arr[[-3,-5,-7]]
print(arr3)

#传递多个索引数组的情况
arr = np.arange(32)
print(arr)
arr = arr.reshape(8,4)
print(arr)

arr2 = arr[[1,5,7,2],[0,3,1,2]]
print(arr2)
#这个例子中的（1,0),(5,3),(7,1)和(2,2)被选中

#常用（理解）
print('arr:\n',arr)
arr2 = arr[[1,5,7,2]][:,[0,3,1,2]]
print(arr2)

#请牢记，神奇索引与切片不同，它总是将数据复制到一个新的数组中

#转置
arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T)

#计算矩阵内积
arr = np.random.randn(6,3)
print(arr)
print(np.dot(arr.T,arr))

'''
对NumPy中dot()函数的理解
如果处理的是一维数组，则得到两数组的内积
如果处理的是二维数组，则得到矩阵积
dot()函数可以通过NumPy库调用，也可以通过数组实例对象进行调用
a.dot(b)与np.dot(a,b)效果相同
矩阵积计算不遵循交换律，np.dot(a,b)和np.dot(b,a)得到的结果是不一样的
'''

#对于更高维的数组，transpose方法可以接收包含轴编号的元组，用于置换轴

arr = np.arange(16).reshape(2,2,4)
print(arr)

#置换轴:第一个轴和第二个轴对换，最后一个轴不变
arr2 = arr.transpose((1,0,2))
print(arr2)

arr3 = arr.transpose((0,2,1))
print(arr3)

#ndarray有一个swapaxes方法，该方法接收一对轴编号作为参数，并对轴进行调整用于重组数据
print(arr)
print(arr.swapaxes(1,2))#参数是轴编号
print(arr.swapaxes(2,1))#参数是轴编号

#swapaxes返回的是数据的视图，而没有对数据进行复制

#通用函数：也称为ufunc，是一种在ndarray数据中进行逐元素操作的函数
arr = np.arange(10)
print(arr)

#一元通用函数示例
print(np.sqrt(arr))
print(np.exp(arr))

#二元通用函数示例
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x,y))
#这里，numpy.maximum逐个元素地将x和y中的元素的最大值计算出来

#使用数组进行面向数组编程
points = np.arange(-5,5,0.01)
print(points)

#生成网格点坐标矩阵
xs,ys = np.meshgrid(points,points)
print(ys)
print(xs)

z = np.sqrt(xs**2 + ys**2)
print(z)

import matplotlib.pyplot as plt
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")

#生成一个随机数组，将数组中所有正值设置为2，所有负值设置为-2
arr = np.random.randn(5,3)
print(arr)
arr = np.where(arr>0,2,-2)
print(arr)
print(arr.sum())
print(arr.mean())

#生成一个随机数组，并求出正值的个数
arr = np.random.randn(5,3)
print(arr)
print((arr>0).sum())

#布尔值数组的any和all方法：
arr = np.array([False,False,True,True,False])
print(arr.all())
print(arr.any())

#排序
#和Python的内建列表类型相似，Numpy数组可以使用sort方法按位置排序：
arr = np.random.randn(6)
print(arr)
arr.sort()
print(arr)

#顶层的np.sort方法返回的是已经排好序的数组拷贝，而不是对原数组按位置排序。
arr = np.random.randn(6)
print(arr)
arr2 = np.sort(arr)
print(arr2)


#pandas入门
import pandas as pd
from pandas import Series, DataFrame

Chinese = pd.Series([90,85,87,80,78])

data = {'Name':['anan','lala','caca','dada','eaea'],
        'Chinese':Chinese,
        'Maths':[89,93,91,86,75],
        'English':[93,97,98,92,90],
        }

frame = pd.DataFrame(data)

print(frame)

#reindex是pandas对象的重要方法，该方法用于创建一个符合新索引的新对象
frame2 = frame.reindex([1,2,3,4,'5','6'])

print(frame)

print(frame2)

print(frame2.head())

#理解这个操作：这里的column、index仅相当于“视图”
frame3 = pd.DataFrame(data,columns = ['CN','MA','EN'],
                      index = ['a','b','c','d','e'])
print(frame3)

'''
5.2.2的drop方法有一个可选参数inplace，默认为False，表明原数组内容并不改变，
如果我们需要得到改变后的内容，需要将新结果赋给一个新的数组。
如果将inplace值设定为True，则原数组内容直接被改变。
'''

print(frame)
frame_no_Chinese = frame.drop('Chinese',axis = 'columns')
print(frame)
print(frame_no_Chinese)

frame.drop('Chinese',axis = 'columns',inplace = True)
print(frame)


#索引、选择与过滤
'''
Series的索引与Numpy数组索引的功能类似，只不过Series的索引值可以不仅仅是整数。
'''

#普通的Python切片是不包含尾部的，Series的切片与之不同：
obj = pd.Series(np.arange(4.),index = ['a','b','c','d'])
print(obj)
print(obj['b':'c'])

#使用这些方法设值时会修改Series相应的部分
obj['b':'c'] = 5
print(obj)

#使用布尔值DataFrame进行索引
data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index = ['Ohio','Colorado','Utah','New York'],
                    columns = ['one','two','three','four'])

#使用单个值或序列，可以从DataFrame中索引出一个或多个列
print(data['two'])
print(data[['three','one']])
print(data[:2])
print(data[data['three'] > 5])

#使用布尔值DataFrame进行索引
print(data)

print(data<5)

data[data<5]=0
print(data)

#使用loc和iloc选择数据
'''
pandas团队创建loc和iloc运算符分别用于严格处理基于标签和基于整数的索引：
轴标签（loc）
整数标签（iloc）
'''
print(data)
#通过标签选出单行多列的数据
print(data.loc['Colorado',['two','three']])
#通过使用整数标签iloc进行类似的数据选择
print(data.iloc[2,[3,0,1]])
print(data.iloc[2])
print(data.iloc[[1,2],[3,0,1]])

#除了单个标签或标签列表之外，索引功能还可以用于切片
print(data.loc[:'Utah','two'])
print(data.iloc[:,:3][data.three>5])

#理解本书 5.2.4整数索引 
ser = pd.Series(np.arange(3.))
#print(ser[-1])，报错
'''
ser的索引包含了0、1、2
所以这种情况下很难推断用户所需要的索引方式是标签索引还是位置索引。
'''

#为了保持一致性，如果你有一个包含整数的轴索引，数据选择时请始终使用标签索引。
ser2 = pd.Series(np.arange(3.),index = ['a','b','c'])
print(ser2[-1])

#为了更精确地处理，可以使用loc(用于标签)或iloc(用于整数)
print(ser[:1])
print(ser.loc[:1])
print(ser.iloc[:1])

#5.25 算术和数据对齐
'''
不同索引的对象之间的算术行为是pandas提供给一些应用的一项重要特性。当你将对象相加时，
如果存在某个索引对不相同，则返回结果的索引将是索引对的并集。
对数据库用户来说，这个特性类似于索引标签的自动外连接（outer join）

没有交叠的标签位置上，内部数据对齐会产生缺失值，缺失值会在后续的算术操作上产生影响。
在DataFrame的示例中，行和列上都会执行对齐。

如果将两个行或列完全不同的DataFrame对象相加，结果全部为空
'''
df1 = pd.DataFrame({'A':[1,2]})
df2 = pd.DataFrame({'B':[3,4]})
print(df1)
print(df2)
print(df1 - df2)

#使用填充值的算术方法
df1 = pd.DataFrame(np.arange(12.0).reshape((3,4)),columns = list('abcd'))
df2 = pd.DataFrame(np.arange(20.0).reshape(4,5),columns = list('abcde'))

print(df1)
print(df2)

df2.loc[1,'b'] = np.nan
print(df2)

#这种情况下，一些不重叠的位置出现NA值
print(df1 + df2)

#在df1上使用add方法，将df2和一个fill_value作为参数传入
print(df1.add(df2,fill_value = 0))

#注意： 表5-5的这些方法中，每一个都有一个以r开头的副本，这些副本方法的参数是翻转的。
'''
理解：因此 1/df1 和 df1.rdiv(1) 这两个语句的结果是等价的
'''
print(1/df1)
print(df1.rdiv(1))

#与此相关的一点，当对Series或DataFrame重建索引时，可以指定一个不同的填充值
#注意:reindex是pandas对象的重要方法，该方法用于创建一个符合新索引的新对象
df3 = df1.reindex(columns = df2.columns , fill_value = 0)
print(df1)
print(df3)

'''
对比: DataFrame和Series间的操作 和 二维数组与一维数组间的操作 
'''

'''
二维数组与一维数组间的操作：
当我们从arr中减去arr[0]时，减法在每一行都进行了操作，这就是所谓的广播机制。
'''
arr = np.arange(12.).reshape((3,4))
print(arr)
print(arr[0])
print(arr - arr[0])

'''
DataFrame和Series间的操作也类似
默认情况下，DataFrame和Series的数学操作会将Series的索引和DataFrame的列进行匹配，并广播到各行。
（理解：默认情况下，Series匹配到DataFrame的某一行，在行上进行广播）
'''
frame = pd.DataFrame(np.arange(12.).reshape((4,3)),
                     columns = list('bde'),index =['Utah','Ohio','Texas','Oregon'])
series = frame.iloc[0]

print(frame)
print(series)
print(frame - series)

'''
想改为在列上进行广播，在行上匹配，需要使用算术方法的某一种。
所传递的axis值用于匹配轴。
下面的示例中表示我们需要在DataFrame的行索引上对行匹配(axis = 'index' 或 axis = 0)，并在列上进行广播
细节：对行匹配 == Series匹配到DataFrame的某一列 
'''
series3 = frame['d']
print(series3)

frame2 = frame.sub(series3, axis = 'index')
print(frame)
print(frame2)

'''
如果一个索引值不在DataFrame的列中，也不在Series的索引中，则对象会重建索引并形成联合。
'''
series2 = pd.Series(range(3),index = ['b','e','f'])
print(frame + series2)

#函数应用与映射
#Numpy的通用函数（逐元素数组方法）对pandas对象也有效
frame = pd.DataFrame(np.random.randn(4,3),columns=list('bde'),
                     index = ['Utah','Ohio','Texas','Oregon'])
print(frame)
print(np.abs(frame))

#另一个常用的操作是将函数应用到一行或一列的一维数组上，DataFrame的apply方法可以实现这个功能

#匿名函数
f = lambda x : x.max() - x.min()
series = frame.apply(f)
print(series)#结果是一个以frame的列作为索引的Series

#如果传递 axis = 'columns' 给apply函数，函数将会被每行调用一次
series2 = frame.apply(f,axis = 'columns')
print(series2)

'''
理解：传递给apply的函数并不一定返回一个标量值，也可以返回带有多个值的Series
'''
def f(x):
    return pd.Series([x.min(),x.max()],index = ['min','max'])
series = frame.apply(f)
print(series)

series2 = frame.apply(f,axis = 'columns')
print(series2)

'''
逐元素的Python函数也可以使用。假设你想要根据frame中的每个浮点数计算一个格式化字符串，
可以使用applymap方法

map、apply和applymap 的区别：
map是将函数套用到Series上的每个元素
apply是将函数套用到DataFrame的行与列
applymap是将函数套用到DataFrame的每个元素

'''
format = lambda x : '%.2f' % x
frame2 = frame.applymap(format)
print(frame2)

'''
使用applymap作为函数名是因为Series有map方法，可以将一个逐元素的函数应用到Series上
'''
series = frame['e'].map(format)
print(series)

#排序与排名 之 排序
#sort_index方法，该方法返回一个新的、排序好的对象
'''
range和arange:
有三个参数，依次为start，end(不包含)，step。在不指明start或者step的情况下，默认起始点为0，步长为1。 
>>> range(2,8,2)
[2, 4, 6]
>>> np.arange(2,8,2)
array([2, 4, 6])

arange返回的是一个ndarray，使用前需要引入numpy，即import numpy as np；而range返回一个list。

arange允许步长为小数，而range不允许 
'''
obj = pd.Series(range(4),index = ['d','a','b','c'])
obj2 = obj.sort_index()
print(obj2)

#如果是根据Series的值进行排序，使用sort_values方法
obj = pd.Series([4,7,-3,2])
obj3 = obj.sort_values()
print(obj3)

#默认情况下，所有的缺失值都会被排序到Series的尾部
obj = pd.Series([4,np.nan,7,np.nan,-3,2])
obj4 = obj.sort_values()
print(obj4)

#在DataFrame中，可以在各个轴上按索引排序
frame = pd.DataFrame(np.arange(8).reshape((2,4)),
                     index = ['three','one'],
                     columns = ['d','a','b','c'])

frame2 = frame.sort_index()
print(frame2)

frame3 = frame.sort_index(axis = 1)
print(frame3)

#数据默认升序排序，也可以按照降序排序
frame4 = frame.sort_index(axis = 1 , ascending = False)
print(frame4)

#对DataFrame排序时，可以使用一列或多列作为排序键
frame = pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print(frame)
frame2 = frame.sort_values(by='b')
print(frame2)
frame3 = frame.sort_values(by=['a','b'])
print(frame3)

#排序与排名 之 排名
'''
Series和DataFrame的rank方法是实现排名的方法。
注意排名中的平级关系打破方法：表5-6
'''

'''
允许存在含有重复标签的轴索引
尽管很多pandas函数（比如reindex）需要标签是唯一的，但这个并不是强制性的。
索引的is_unique属性可以告诉我们它的标签是否唯一
带有重复索引的情况下，数据选择与之前的操作有差别：根据一个标签索引多个条目会返回一个序列，
而单个条目会返回标量值。
相同的逻辑可以拓展到在DataFrame中进行行索引
'''
#描述性统计的概述与计算
#相关性和协方差
#唯一值、计数和成员属性
obj = pd.Series(['c','a','d','a','a','b','b','c','c'])
uniques = obj.unique()
print(uniques)

'''
Python sort和sorted :
list内置sort()方法用来排序，也可以用python内置的全局sorted()方法来对可迭代的序列排序生成新的序列。
sort()不能对dict字典进行排序。
使用sorted()对dict排序默认会按照dict的key值进行排序，最后返回的结果是一个对key值排序好的list。

示例：

my_dict = {"a":"2", "c":"5", "b":"1"}

result = sorted(my_dict)
print result
#默认对dict排序，不指定key参数,会默认对dict的key值进行比较排序
#result输出: ['a', 'b', 'c']

result2 = sorted(my_dict, key=lambda x:my_dict[x])
print result2
#指定key参数，根据dict的value排序
#result2输出:['b', 'a', 'c']

'''
uniques.sort()
print(uniques)

#value_counts计算出Series包含的值的个数
#为了方便，返回的Series会按照数量降序排序
series_counts = obj.value_counts()
print(series_counts)

print('value_counts也是有效的pandas顶层方法，可用于任意数组或序列')
series_counts2 = pd.value_counts(obj,sort=False)
print(series_counts2)

print('isin执行向量化的成员属性检查，还可以将数据集以Series或DataFrame一列的形式过滤为数据集的值子集')
print(obj)

mask = obj.isin(['b','c'])
print(mask)
print(obj[mask])#??????????????????????????????

print('与isin相关的Index.get_indexer方法')
'''
Index.get_indexer 方法的含义：
表示to_match中的字符，在unique_vals中的位置索引。
博客：https://www.cnblogs.com/rougan/p/10071537.html
'''
to_match = pd.Series(['a','c','d','c','b','d','a','c','a'])
unique_vals = pd.Series(['a','b','c','d'])
index_list = pd.Index(unique_vals).get_indexer(to_match)
print(index_list)

#最后一种情形
data = pd.DataFrame({'Qu1':[0,3,4,3,4],
                     'Qu2':[2,3,1,2,3],
                     'Qu3':[1,5,2,9,4,]})
print(data)

#将pandas.value_counts传入DataFrame的apply函数可以得到：
result = data.apply(pd.value_counts).fillna(0)
print(result)
'''
尝试写出运行结果：
   Qu1  Qu2  Qu3
0  1.0  0.0  0.0
1  0.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  1.0
5  0.0  0.0  1.0
9  0.0  0.0  1.0

这里，结果中的行标签是所有列中出现的不同的值，数值则是这些不同值在每个列中出现的次数。
'''

#数据载入、存储及文件格式

'''
文本格式数据的读写
'''

'''
Unix shell的cat命令用来显示文件的内容
在Windows下，可以使用type来代替cat达到同样的效果
'''

'''
使用read_csv将数据读入一个DataFrame
'''
df = pd.read_csv('examples/ex1.csv')
print(df)

'''
有的文件并不包含表头行
要读取该文件，需要选择一些选项：
可以允许pandas自动分配默认列名，也可以自己指定列名
'''
df2 = pd.read_csv('examples/ex2.csv',header = None)
print(df2)

df3 = pd.read_csv('examples/ex2.csv',names = ['a','b','c','d','message'])
print(df3)

#此处是不准确示范
df4 = pd.read_csv('examples/ex2.csv')
print(df4)

'''
若要把message列成为所返回的DataFrame的索引，可以指定该列为索引
'''
names = ['a','b','c','d','message']
df5 = pd.read_csv('examples/ex2.csv',names=names,index_col='message')
print(df5)

'''
若要从多个列中形成一个分层索引，需要传入一个包含列序号或列名的列表
'''
parsed = pd.read_csv('examples/csv_mindex.csv',index_col=['key1','key2'])
print(parsed)

'''
一张表的分隔符并不是固定的，有的则是使用空白或其他方式来分隔字段。
'''
l = list(open('examples/ex3.txt'))
print(l)

'''
当字段是以多种不同数量的空格分开时，尽管你可以手工处理，
但在这些情况西安也可以向read_table传入一个正则表达式作为分隔符。
在本例中，正则表达式为\s+
'''
result = pd.read_table('examples/ex3.txt',sep='\s+')
print(result)
'''
本例中，由于列名的数量比数据的列数少一个，因此read_table推断第一列应当为DataFrame的索引
'''

#解析函数有很多附加参数帮助你处理各种发生的异常的文件格式
#本书表6-2：一些read_csv/read_table函数的参数 列举了一部分

#使用skiprows:从文件开头处起，需要跳过的行数或行号列表
df6 = pd.read_csv('examples/ex4.csv',skiprows = [0,2,3])
print(df6)

#缺失值处理
result = pd.read_csv('examples/ex5.csv')
print(result)
result_isnull = pd.isnull(result)
print(result_isnull)

#na_values选项可以传入一个列表或一组字符串来处理缺失值
result2 = pd.read_csv('examples/ex5.csv',na_values=['NULL'])
print(result2)

'''
理解函数na_values的含义，别搞混了
na_values:需要用NA替换的值的序列
'''
result3 = pd.read_csv('examples/ex5.csv',na_values = ['11.0'])
print(result3)

#在字典中，每列可以指定不同缺失值标识
sentinels = {'message':['foo','NA'],'something':['two']}
result4 = pd.read_csv('examples/ex5.csv',na_values = sentinels)
print(result4)

#表6.2列举了pandas.read_csv和pandas.read_table中常用的选项

'''
分块读入文本文件
'''

#对pandas的显示设置进行调整
pd.options.display.max_rows = 10

result = pd.read_csv('examples/taobao_data.csv')
print(result)

#如果你只想读取一小部分行（避免读取整个文件），可以指明nrows
result = pd.read_csv('examples/taobao_data.csv',nrows = 5)
print(result)

'''
为了分块读入文件，可以指定chunksize作为每一块的行数
read_csv返回的TextParser对象允许你根据chunksize遍历文件
TextParser还具有get_chunk方法，允许你按照任意大小读取数据块
'''

chunker = pd.read_csv('examples/taobao_data.csv',chunksize = 2000)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['成交量'].value_counts(),fill_value = 0)
tot = tot.sort_values(ascending = False)
print(tot[:10])

'''
将数据写入文本格式
'''
data = pd.read_csv('examples/ex5.csv')
print(data)

'''
使用DataFrame的to_csv方法，我们可以将数据导出为逗号分隔的文件
'''
data.to_csv('examples/out.csv')

'''
当然，其他分隔符也是可以的(写入到sys.stdout时，控制台中打印的文本结果)
'''
import sys
data.to_csv(sys.stdout,sep = '|')

'''
缺失值在输出时以空字符串出现，也可以用其他标识符对缺失值进行标注
'''
data.to_csv(sys.stdout,na_rep='NULL')

'''
可以禁止写入行和列的标签
'''
data.to_csv(sys.stdout,index=False,header=False)

'''
可以仅写入列的子集，并按照你选择的顺序写入
'''
data.to_csv(sys.stdout,index=False,columns=['a','b','c'])

'''
Series也有to_csv方法
'''
dates = pd.date_range('1/1/2000',periods=7)

ts = pd.Series(np.arange(7),index=dates)

ts.to_csv(sys.stdout)

'''
使用分隔格式

绝大多数的表型数据可以使用函数pandas.read_table从硬盘中读取
然而，接收一个带有一行或多行错误的文件并不少见，read_table并不能解决这种情况

对于任何带有单字符分隔符的文件，你可以使用Python的内建csv模块。
要使用它，需要将任一打开的文件或文件型对象传给csv.reader
'''
import csv
f = open('examples/ex7.csv')
reader = csv.reader(f)

'''
像遍历文件一样遍历reader会产生元组，元组的值为删除了引号的符号
'''
for line in reader:
    print(line)

'''
将文件读取为行的列表
'''
with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))
print(lines)

'''
将数据拆分成列名行和数据行
'''
header, values = lines[0], lines[1:]
print(header)
print(values)

'''
使用字典推导式和表达式zip(*values)生成一个包含数据列的字典，字典中的行转置为列
'''
data_dict = { h: v for h, v in zip(header, zip(*values))}
print(data_dict)





















