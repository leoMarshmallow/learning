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
r1 = reduce(lambda x,y:x+y,[1,3,5,6],1)
print(r1)

# 关于函数的注解使用
# 格式为：def fun(param1:***,param2:***)->***:
def f(p1:"string",p2:"string")->"string":
    print("注解为",f.__annotations__)
    print(p1+p2)
f("aa","bb")