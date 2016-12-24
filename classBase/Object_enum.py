#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'枚举类'

from enum import Enum

month = Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                        'Sep', 'Oct', 'Nov', 'Dec'))
# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6