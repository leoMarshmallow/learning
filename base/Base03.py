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