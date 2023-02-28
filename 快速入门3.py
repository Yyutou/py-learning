"""
python序列
"""
"""
》序列：一块可以存放多个值的连续内存空间，这些值按一定顺序排列，可以通过每个值所在位置的索引访问他们
》序列中的每个值都有对应的位置值，即索引
》常用序列：列表，元组，字典，集合
》常用操作：索引，长度，组合，重复，切片，检查成员，遍历，最大最小值
"""
#列表
#用[]表示，可以嵌套
a = [1,3,2,1]
print(a)
print(a[0])
b = ['A',123,True,231.7]
print(b)
c = [['sad ',123],[31,412],2313]
print(c) 

#创建一个列表
a = [1,23,23]
a = []
#使用list()函数将元组，range对象，字符串等转换为列表
a_list = list((3,2,5,19))
b_list = list(range(1,10,1))
c_list = list('sakdhakubkfa')
d_list = list()
print(c_list)

#列表的访问
#使用下标索引访问列表的元素
#从左到右0开始，从右到左-1开始
A_list = ['123','ndnakjsd',213]
print(A_list[1],A_list[-1])
#修改访问的元素
A_list[0]=1
print(A_list)

#常用功能
a =['tree','plant','transplant']
#insert(index,value)在index位置之前插入value
a.insert(2, '...')
print(a)
#extend 末尾添加
a.extend('iterable')
print(a)
#pop(index) 取出index位置的元素
a.pop(4)
print(a)
#remove 删除元素
a.remove('...')
print(a)
#clear 清空列表
a.clear()
print(a)

a=['asad','be','a','like','forever','a']
#count(value) 计算value值的个数
n=a.count('a')
print(n)
#index(value) 计算value值对应的下标
n=a.index('asad')
print(n)
m=a.index('a')
print(m) 
#sort() 排序,按照字典的顺序排序，后面有详细的说明
a.sort()
print(a)
#reverse() 翻转
a.reverse()
print(a)
#copy() 复制
d= a.copy()
print(d) 

#检查成员
a=[1,2,3,4,5,5,11]
b = 3 in a
print(b)
b = [3] in a
print(b)
b = 22 not in a
print(b)

#切片 [初始位置:终止位置:步长]
a=[1,2,3,4,5,5,11]
b=a[::2]
print(b)
b=a[::-1]    #逆序输出
print(b)

#复制
from copy import *
a =[1,3,1,3,['abcd','qwer']]
b = a 
c = copy(a)        #浅拷贝，修改原来的值会一起修改，但不会新增
d = deepcopy(a)    #深拷贝，最原始的值
a.append(5)
a[4].append('yy')
print(a,'\n',b,'\n',c,'\n',d,'\n')

#排序
from random import *
a=list(range(20))
shuffle(a)    #打乱顺序，原地
print(a)

a.sort()    #升序排序，原地
print(a)

a.sort(reverse=True)    #降序排序，原地
print(a)

b=sorted(a)    #生成一个新列表，升序排序
print(b)

b=sorted(a,reverse=True)    #生成一个新列表，升序排序
print(b)

#内置函数：len,sum,max,min

"""
"""
#元组tuple()
#有序，不可变序列；用()表示
a=(90,92,98,20)
print(a,type(a))
b=('231','asda',True,(123,12))
print(b,type(b))

#创建与删除
#创建参考list
#删除只能删除整个元组，使用del

""""""
#集合set{}
#无序 不能重复
#add()
#remove()
#pop()