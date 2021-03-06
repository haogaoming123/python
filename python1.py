#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello,world')

#输入函数input()
name = input('请输入你的名字:') 
print('name =', name)
#练习:请利用print()输出1024 * 768 = xxx
print('1024 * 768 =',1024*768)

print('''world1
world2
world3''')

x = 100
x = x - 10
print('x =',x)

print(ord('中'))
print('\u4e2d\u6587')
print(chr(66))

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xe6\x96\x87abc'.decode('utf-8', errors='ignore'))

#计算字符串个数
print('你的名字有',len(name),'个字')

#格式化字符串
print('hello,%s,how are you,我有%d句话对你说,你还有%.2f元' % (name,5,5.5))
print('年化利率为：%.2f%%' % 4.99)
#format()格式化字符串
print('hello,{0},成绩提升了{1:.2f}%'.format(name,17.125))
#练习题目
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('小明成绩提升了%.1f%%' % r)


###数组
classmates = ['Michael', 'Bob', 'Tracy']
print('数组为:',classmates)
print('数组1：',classmates[0],'数组2：',classmates[1],"数组3：",classmates[2])
classmates.append(123)	#添加数组元素
print('变更后的数组为1:',classmates)
classmates.insert(0,3)  #插入指定位置的数组
print('变更后的数组为2:',classmates)
classmates.pop(3)  #删除数组元素
print('变更后的数组为3:',classmates)


###元祖
yuanzu = ('元组1','元组2','元组3')
print('元组为：',yuanzu)
#yuanzu[0] = 123 ---错误写法，元组复制后不可改变

##创建一个改变的元组
yuanzu2 = ('123','231',['1','2'])
yuanzu2[2][0] = 34
yuanzu2[2][1] = 12
print('元组为：',yuanzu2)

##调节判断语句
if len(yuanzu2) > 3:
	print('元组个数大于3个')
	print('元组个数大于3个')
elif len(yuanzu2) == 3:
	print('元组个数为3个')
else:
	print('元组个数不大于3个')
print('end')

##判断小明的体重指数
weight = input('请输入你的体重(公斤)：')
height = input('请输入你的身高(米)：')
bmi = float(weight) / float(height) / float(height)
if bmi > 32:	
   print(name,',你严重肥胖')
elif bmi >= 28 and bmi < 32:
   print(name,',你比较肥胖')
elif bmi >= 25 and bmi < 28:
   print(name,',你体重过重')
elif bmi >= 18.5 and bmi < 25:
   print(name,',你体重正常')
elif bmi < 28:
   print(name,',你体重过轻')

##循环
for name in yuanzu2:
	print('元素：',name)

sum = 0
for x in range(4):
	print(x)
	sum += x
print('总和为：',sum)

##字典
dic = {'key1':95,'key2':93,'key3':94}
for key in dic:
	print(key)
for value in dic.values():
	print(value)
for key,value in dic.items():
	print(key,'=>',value)

a = 'abc'
a = a.replace('a','A')
print('a=',a)

##定义函数：#数据类型检查函数：isinstance()#
def my_abs(x):	
	if not isinstance(x, (int, float)):
		raise TypeError('不是整型或浮点型数字，阻断后续程序的执行')
	if x < 0:
		return -x
	else:
		return x
print(my_abs(-99))

##函数返回多个值
import math #导入包
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
nx, ny = move(100, 100, 60, math.pi / 6)
print(nx,ny)

##默认参数
def add_end(L=None,n=2):
	if L is None:
		L = []
	L.append(n)
	L.append('end')
	return L
print(add_end())
print(add_end(n=3))

##可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n 
	return sum
print('可变参数：',calc(1,2,3,4))
print('可变参数：',calc())

##关键字参数
def person(name, age, **kw):
	#说明：**kw 将后边的传入参数自动组装为一个字典tuple
	print('name:',name,'age:',age,'other:',kw)
person('小马','18',job='IT')
yuanzu3 = {'city':'beijing','job':'IT'}
person('小马','18',**yuanzu3) ## **yuanzu表示把元祖所有的key->value用关键字传入**KW

##命名关键字参数
print('--省略---')

##递归函数
def fact1(n):
	if n == 1:
		return 1
	return n * fact1(n-1)
print(fact1(10))

##尾递归优化：防止递归导致栈溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(10))
#说明：Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

'''
汉诺塔的移动可以用递归函数非常简单地实现。
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。
'''
def move(n, a, b, c):
    if n == 1:
        print ('%s --> %s' % (a, c))
    else:
        move(n - 1, a, c, b)    # 简化问题
        move(1, a, b, c)        # 移动最下面的大盘子
        move(n - 1, b, a, c)

if __name__ == '__main__':
    move(3, 'A', 'B', 'C')

##迭代，enumerate函数把数组变为索引-元素
for x,val in enumerate([1,2,3,4,5]):
	print('索引',x,'==>',val)


##查找最大值和最小值
def findMinAndMax(L):
	if len(L) == 0:
		return (None,None)
	min = L[0]   #最小值
	max = L[0]   #最大值
	for x in L:
		if x >= max:
			max = x
		if x <= min:
			min = x
	return (min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
		

##列表生产器
import os
array = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(array)

d = {'x':'A','y':'B','z':'C'}
arrayK = [k+'==>'+v for k,v in d.items()]
print(arrayK)


##map(f,Iterator)函数:第一参数为函数，第二参数为可循环的参数
def fff(x):
	return x * x
result = map(fff,[1,2,3,4,5,6,7,8,9])
print('result:',list(result))  ##list()函数可以序列化map返回的值

##reduce函数，将一次的计算结果序列化到下一次继续计算
from functools import reduce 
def add(x , y ):
	return x + y
reduceResult = reduce(add,[1,3,5,7,9])
print('reduce的结果：',reduceResult)

#sorted函数:
#key:根据key函数返回结果排序
#reverse=True：反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)













