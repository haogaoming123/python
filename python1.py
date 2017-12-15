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











