#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
进制转换
'''


'''
二进制    0b101
     以数字0和字母b打头的表示二进制数 如果出现大于等于2的数 会抛出SyntaxError异常
八进制    0o711
     以数字0o打头的数字表示八进制数 如果出现大于等于8的数 会抛出SyntaxError异常
十进制    123
     正常显示 不能出现字母
十六进制  0x15
     以数字0和字幕x打头的表示十六进制数 可以出现0-9和abcdef或ABCDEF出现其他数值会
     抛出SyntaxError异常
'''

# 10进制转换为2进制
print(bin(3))

# 2进制转换为10进制
print(int('1001',2))

# 10进制转为16进制
print(hex(15))

# 16进制转为10进制
print(int('0x11',16))

# 10进制到8进制
print(oct(10))

# 8进制转为2进制
print(bin(0o10))