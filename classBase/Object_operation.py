#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'对对象的操作'

class Music(object):

    def __init__(self,name,type):
        self.__name = name
        self.type = type

    def get_name(self):
        return self.__name

dream = Music("dream","EDM")
print(dir(dream))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法：

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，len('ABC')和'ABC'.__len__()是等价的：
dream.language = "CN"
# hasattr方法不能判断私有属性
print(hasattr(dream,"type"))
# getattr：获取属性，setattr：更新属性或者新增（公共）属性
setattr(dream,"__name","nono")
print(dream.get_name())
setattr(dream,"is_hot",True)
print(getattr(dream,"__name"))
print(getattr(dream,"is_hot"))
# getattr可以传入default参数，如果不存在该属性则返回默认擦参数
print(getattr(dream,"album","anon"))
# getattr也可以用来获得对象的方法
get_name = getattr(dream,"get_name")
print(get_name())

# 下面是正确获得对象的方法或者属性：
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None

# 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性
# 将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


def set_author(self,author):
    self.author = author

# 给实例绑定一个方法：
from types import MethodType

dream.set_author = MethodType(set_author,dream)
dream.set_author("dj saozhu")
print(dream.author)

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性：

class SlotsObject(object):
    __slots__ = ("name","age")

so = SlotsObject()
so.name = "so"
# so.sex = 0 这句话执行是会报错，因为该对象只被允许绑定name属性

# 要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了
# 另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个
# 可控的属性操作：
class PropObject(object):

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise ValueError("age must be a integer!")
        if age < 0 or age > 110:
            raise ValueError("age must between 0 and 110!")
        self.__age = age

gigi = PropObject()
gigi.age = 0
print(gigi.age)

# 当然也可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性。

class Movie(object):
    def __init__(self,name,language):
        self.__name = name
        self.__language = language

    def __str__(self):
        return 'Movie object (name: %s)' % self.__name

    def __call__(self, *args, **kwargs):
        print("callable")

print(Movie("the great wall","CN"))

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。我们以斐波那契数列为例：
class Fib(object):
    def __init__(self):
        self.x, self.y = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.x, self.y = self.y, self.x + self.y
        if self.y > 100:
            raise StopIteration()
        return self.x



for i in Fib():
    print(i)

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用，如：s()

# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否
# 能被调用，能被调用的对象就是一个Callable对象，
print(callable(Movie("aa","CN")))