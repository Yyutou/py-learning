"""
   python快速入门
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