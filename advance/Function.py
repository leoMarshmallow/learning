# 定义一个函数
def plus(a,b):
    return a+b
# 调用这个函数
p = plus
print(p(2,3))
# 可以通过=来重命名函数

def noResult():
    pass
print(noResult())
# 没有返回值的函数也会返回一个none

# 默认参数值
# def defalutPara(flag,boy='leo',girl='xyc'):
#     if flag in ('y','yes','yeah'):
#         return boy+' like '+girl
#     if flag in ('n','no','not'):
#         return boy+' dislike '+girl
#     else:
#         raise ValueError('格式错误了啊大哥')
# print(defalutPara(input()))

# 关于默认参数值是只计算一次，但是对于列表、字典或类的实例等易变对象是则会发生变化
a = 1
def f1(param=a):
    print(param)
a = 2
f1()
list1 = [1,2]
def f2(param=list1):
    print(param)
list1.append(3)
f2()

# *param 表示将除关键字参数以外的可变位置参数装入元祖中，
# **param 表示接受除形参以外的可变关键字参数
def multiFun(job,*hobby,**skill):
    print("introduce yourself to be",job)
    print("="*20)
    for h in hobby:
        print(h)
    else:
        print("="*20)
    keys = skill.keys()
    for k in keys:
        print(k,"---",skill[k])
multiFun("java developer","games","movies","comics",java="skillful"
         ,html="skillful",python="greenhand")

# lambda 关键字起到一个函数速写的作用
f = lambda x,y:x+y
print(f(1,2))

# lambda表达式也可放在函数中

# reduce 表示连续对sequence执行function，如果有initial则从initial开始
from functools import reduce
r1 = reduce(lambda x,y:x+y,range(101))
print(r1)
print(sum(range(101)))

# 关于函数的注解使用
# 格式为：def fun(param1:***,param2:***)->***:
def f(p1:"string",p2:"string")->"string":
    print("注解为",f.__annotations__)
    print(p1+p2)
f("aa","bb")

# 可以把函数当做参数传入，如：
def add(a, b, f):
    print(f(a) + f(b))
add(-1, 2, abs)

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到
# 序列的每个元素，并把结果作为新的Iterator返回。
print(list(map(abs, [-1, -2, 9, -4])))

# 将首字母大写
def nameNormalize(name):
    return name.upper()[0] + name.lower()[1:]
print(list(map(nameNormalize,['adam', 'LISA', 'barT'])))

# 将字符串转为小数
strList = list("123.56")
index = len(strList) - strList.index('.') - 1
strList.remove(".")
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, \
        '8': 8, '9': 9}[s]
re = reduce(lambda x, y:x*10 + y, map(char2num, strList))
print(re/(10**index))

# str.strip(s),删除str字符串开头、结尾处中包含s的字符，默认可以去空，如：
print("abcdef".strip("def"))
print("abcdef".strip("bc"))
print("abcdef".strip("ba"))
print("  abcde f ".strip())
print(" ".strip().__len__())

# filter()函数用于过滤序列。和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是
# False决定保留还是丢弃该元素。
def not_empty(str):
    return str and str.strip()
print(list(filter(not_empty,["a", "", "b", None])))

# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator
# 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动
# 调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句
# 就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像
# 一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的
# 迭代值。yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，
# 比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰

# 埃氏筛法来获得素数
# 先定义一个从3开始的基数生成器
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def _not_divisible(n):
    return lambda x: x % n > 0

for i in primes():
    if i < 20:
        print(i)
    else:
        break

print(list(filter(lambda x: x % 3 > 0, [3, 5, 7, 9])))

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# 用切片的方法来获得list的反转
print(list(filter(lambda i:str(i) == str(i)[::-1],range(102))))