"""
   python快速入门1
"""

"""
python变量
"""
#命名规则：
# 字母或下划线开头    注：下划线开头有特殊含义；不能以数字开头
# 不能有空格或标点符号
# 不能与关键字重名
# 不与内置名称相同
# 大小写敏感
# 名称取得有意义

x = 20    #整型变量
y = 40    #整型变量
s = 'Wherever you are'    #字符串型变量
t = 20.3    #浮点数型变量
flag = True    #布尔型变量 只有两个True和False

print(flag)
print(x + y)
print(s)
print(t)


"""
数字
"""
# 不可变对象
# 整数，浮点数，复数
# 整数可以任意大

print(2 + 4)
print(123 - 342)
print(20 + 4 * 5)

print(4 / 2)
print(3 // 2)
print(4 // 2)

print(3 / 2)
print(3 % 2)
print(2 ** 10)

print(2 ** 128)

"""
进制转换
"""
#使用int函数转到十进制，包含两个参数，int（参数1，参数2）
#参数1：字符串类型，表示待转换的数
#参数2：待转换数的数值类型
print(int('0b11010101',2))
print(int('0o43124',8))
print(int('0xFF12F',16))

print(bin(432))
print(oct(432))
print(hex(432))

print(bin(0xFF12F))
print(hex(0o43124))
print(0b1011011)

#print直接输出十进制数
print(0o53)
print(0xF01d)


"""
带格式打印，左右对齐
"""
x = 1234.56789
print(format(x,'0.2f'))    #保留小数点后2位1234.57

print(format(x,'<12.2f'))    #保留小数点后2位，在12个字符长度的区间内向左对齐，右侧空格

print(format(x,'0<12.2f'))    ##保留小数点后2位，在12个字符长度的区间内向左对齐，右侧补0

print(format(x,'1<12.2f'))    ##保留小数点后2位，在12个字符长度的区间内向左对齐，右侧补1

print(format(x,'啊<12.2f'))    ##保留小数点后2位，在12个字符长度的区间内向左对齐，右侧补啊

print(format(x,'>12.1f'))    #保留小数点后1位，在12个字符长度的区间内向右对齐，左侧补空格

print(format(x,'0>12.1f'))    #保留小数点后1位，在12个字符长度的区间内向右对齐，左侧补0

print(format(x,'^12.3f'))    #保留小数点后3位，在12个字符长度的区间中间对齐，两侧侧补空格

print(format(x,'0^12.3f'))    #保留小数点后3位，在12个字符长度的区间中间对齐，两侧侧补0

print(format(x,',.2f'))    #保留2位小数，加上千分位逗号

print(format(x,'e'))    #科学计数法

print(format(x,'.2e'))    #保留2位小数，科学计数法

print(format(x,'0.2e'))    #保留2位小数，科学计数法

print(format(x,'.2E'))    #保留2位小数，科学计数法

"""
    字符串

转义字符：\
使用f去除转义符号
+ 字符串拼接
* 字符串重复
"""
print('ab'*3)
print([1,2,3]+[3,4,6])

"""
    运算符和表达式
"""
#逻辑运算
a = 5
b = 2
print(a == b)
print(a != b)
print(a > b)

print(a < b)
print(a >= b)
print(a <= b)

a = 1
b = -1
print(a and b)    #只要a不等于0，就打印b的值
print(a or b)    
print(not a)

#位运算
a = 0b00111100
b = 0b00001101
print(bin(a & b))    #与
print(bin(a | b))    #或
print(bin(a ^ b))    #异或

print(bin(a << 2))    #左移2位
print(bin(a >> 2))    #右移2位

print(bin(~ a))    #按位取反,
print(~5)          #输出-6，取反后用补码表示

#成员运算符 in/not in 
a = 3
b = 20
list = [1,2,3,4,5]
if (a in list):
       print('True')
if (b in list):
       print('True')

t='True'
f='False'
print(t if (a in list) else f)
print(t if (b not in list)else f)

#身份运算符 is /is not
a=2
b=3
c=2
if (a is not b):print(t)
if(a is c):print(t)

#常用内置函数
print(pow(2,3))    #2的3次方
print(abs(-33))    #绝对值
print(round(3.7))    #四舍五入
print(round(3.3))
"""
ord():打印ASCII码
chr():打印字符
max,sum,len,bin,oct,hex
"""

#基本输入输出 input() print()
#input()默认string类型

