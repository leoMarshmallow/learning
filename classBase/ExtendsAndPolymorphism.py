#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'继承与多态概念，练习'

class Animal(object):

    def run(self):
        print("An Animal is running")

class Cat(Animal):

    def run(self):
        print("A dog is runnig")

    def bark(self):
        print("fuck off")

class Dog(Animal):

     def run(self):
         print("A cat is running")

     def attack(self):
         print("fucking shit man!")


cc = Cat()
cc.run()
cc.bark()

dd = Dog()
dd.run()
dd.attack()

# 和java一样存在着重写父类方法的特点
# 多态的好处是什么呢，可以再声明参数为父类的时候，根据传入的子类实例来实现不同的目的
# 这就是符合开发中推荐的“开闭原则”，即对扩展开放，对修改封闭

# ========静态语言 vs 动态语言=========
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型
# 或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有
# 一个run()方法就可以了：