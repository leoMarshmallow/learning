#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'类、对象的基础'

class Student(object):
    pass

# class 类名(object)：表示继承自object

# 实例化：
lv = Student()
print(lv.__class__)

# 可以自由地给一个实例变量绑定属性，比如，给实例lv绑定一个skill属性
lv.skill = "bibi"
print(lv.skill)

# 可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的
# __init__方法，在创建实例的时候，就把属性绑上去：
# __str__的作用类似于java中的toString
class Programmer(object):

    def __init__(self,name,skill):
        self.name = name
        self.skill = skill

    def __str__(self):
        return 'Programmer (name: %s)' % self.name

leo = Programmer("leo", "java")
print(leo.skill,leo.name)
print(leo)

# Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的
# 不同实例，但拥有的变量名称都可能不同

# 现在programmer的属性是可以被被外部代码修改的
leo.name = "fucking man"
print(leo.name)

# 要使得这些变量受到保护，即私有化，可以在变量名前加__，如：
class Boy(object):
    def __init__(self,name,sex):
        self.__name = name
        self.sex = sex

    def introBoy(self):
        print(self.__name,self.sex)

lyl = Boy("lyl","man")
lyl.introBoy()
lyl.sex = "woman"
lyl.__name = "lll"
lyl.introBoy()

# 可以发现__name没有发现变化

# 但是当外部需要获取这些属性的时候就需要get，set方法来进行操作，如：
class StrongBoy(object):

    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

sb = StrongBoy("naima")
print(sb.get_name())
sb.set_name("xsl")
print(sb.get_name())

# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然
# 可以通过_Student__name来访问__name变量：
print(sb._StrongBoy__name)
# 但是强烈建议你不要这么干

# 这时候对sb赋一个__name,这时候已经不再是之前那个__name,而是一个新的变量

