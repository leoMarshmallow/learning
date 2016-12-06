#print(10/3,10//3,10%3)
# 1. 输出print

# str = input()
# 输入input()

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义,如:`print(r'\\\t\\')`
# python中的空位none
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头

print(9/3,10//3,10%3)
# /除法:除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数,如:`9 / 3 -> 3.0`
# //除法,称为地板除，两个整数的除法仍然是整数,如:`10 // 3 -> 3`
# %除法为取余


# `"#!/usr/bin/env python3 # -*- coding: utf-8 -*-"`,第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，
# Windows系统会忽略这个注释.
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

print('hi, %s, you have $%d.' % ('michael', 1000000))
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
# 后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略.

print('%.2f   %d' % (3.1415926, 1))
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

# list用[]定义,tuple元组用()定义
# 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改,代码更安全
# t=(1)定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
# 因此，python规定，这种情况下，按小括号进行计算，计算结果自然是1。所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义

# dict类似于map,在python中叫做数据字典,dict内部存放的顺序和key放入的顺序是没有关系的。

# if-elif-else

# 定义函数如下:
# def add(a,b):
# 	return a+b

# 调用函数如下
# from add import add
# print(add(1.1,2))

# pass可以定义一个空函数,可以用来做占位符使逻辑正常执行,如下:
# def judge(flag):
# 	if not isinstance(flag,(int)):
# 		raise TypeError('bad type')
# 	if flag > 0:
# 		return 1
# 	elif flag == 0:
# 		return 0
# 	else:
# 		pass

# 函数可以返回多个值其实就是一个tuple

# `import math`可以使用如`math.sqrt(a)`来求平方根等

# 默认参数
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
# #调用时可以不填默认参数如:
# enroll('lili','F',city='hb')

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！,用None修改如下:
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# 可变参数的用法,再参数名前加*,得到tupel
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# `*args`是可变参数，`args`接收的是一个`tuple`;`**kw`是关键字参数，`kw`接收的是一个`dict`。

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，
# 所以就不是尾递归了。

#print(2**3)
# **表示乘方

#print(r"i'm \=./")
# r加字符串表示使用原始字符串

# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
# 通过""" """可以更灵活的排版

#print(3*"a"+2*"b")
## 可以通过*+来拼接字符串

#print("a""b")
# 两个引号相邻的字符串会自动拼接起来

# word = '你呢？'
# print(word[0])
# print(word[-1])
# print(word[0:2])
# print(word[1:])
# print(len(word))
# 字符串可以直接使用索引，为负数的索引都是从最右开始,而且支持灵活的切片
# word[0] = 'o'
# Python 字符串不能更改 — — 他们是 不可变的。因此，赋值给字符串索引的位置会导致错误

numbers = [1,2,3]
numbers+=[4,5]
numbers.append(6)
numbers[2:4]=['a']
print(numbers)
a = ['aaa',numbers]
print(a)