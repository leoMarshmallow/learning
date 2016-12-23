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
    __slots__ = ("name")

so = SlotsObject()
so.name = "so"
so.sex = 0 # 这句话执行是会报错，因为该对象只被允许绑定name属性

# 要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的