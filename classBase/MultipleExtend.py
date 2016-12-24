#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多重继承'

class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass


# 不同动物的能力
class Runnable(object):
    def run(self):
        print("running...")

class Flyable(object):
    def fly(self):
        print("flying...")

# 多重继承
class Dog(Mammal,Runnable):
    pass

class Cat(Mammal,Runnable):
    pass

class Eagle(Bird,Flyable):
    pass

class Bat(Mammal,Flyable):
    pass

Dog().run()
# 这种设计通常称之为MixIn