"""
    python快速入门2 
"""

#选择与循环

"""选择结构
(一)单分支
  输入两个数，从小到大输出
（二）双分支
  已知鸡兔总数量和腿的数量，求鸡兔共多少只
（三）多分支
求绩点，输出（优秀4，良好3，中等2，及格1，不及格<1）
（四）嵌套
"""
#(一)
x = input('Input two numbers:')
a,b = map(int,x.split())
if a > b:
    a,b=b,a
print(a,b)

#(二)
h = int(input('请输入鸡兔总数量：'))
f = int(input('请输入腿的总数量：')) 
tu = int(f/2-h)
ji = int(h-tu)
if (tu<0 or ji<0 or ji*2+tu*4 != f):
    print('输入有误')
else:
    print("鸡兔数量为:",ji,tu)

#(三)
score = int(input("请输入你的成绩："))
l = score/10 - 5
if l >= 4: print(4)
elif l >= 3: print(3)
elif l >= 2: print(2)
elif l >= 1: print(1)
else: print(0)

"""循环结构
while
for

"""
#求表达式的值：1+1/3+1/3*2/5+1/3*2/5*3/7+..
pi,t,n=0.0,1.0,1
while n<100:
    pi=pi+t
    t=t*n/(2*n+1)
    n+=1
print(2*pi)

#for
word='Hello world'
for i in word:
    print(i)
for i in word:
    print(i,end='')

#for 配合range函数使用
#range(初始值，终止值，步长)不设置则默认；含头不含尾
#初值大于终值，序列为空,不会打印
for i in range(1,10,1):
    print(i,end=' ')
for i in range(10,1):
    print(i)

#求n的阶乘
n=int(input())
fac=1
for i in range(1,101,1):
    fac*=i
print('%d!=%d'%(n,fac))

#break语句，无条件的跳出整个循环
s_list = []
while True:
    score=int(input())
    if score == -1:
        break
    s_list.append(score)
print(s_list)

#continue语句，跳过当前循环块中的剩余语句，然后继续进行下一轮循环
sum,n=0,0
for i in range(4):
    a=int(input())
    if a<=0:
        continue
    sum=sum+a
    n=n+1
print(sum,n)

#水仙花数
for i in range(152,1000,1):
    a = i // 100
    b = i // 10%10
    c = i % 10
    if i == a**3+b**3+c**3:
        print(i)