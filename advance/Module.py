#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块是包含 Python 定义和声明的文件。文件名就是模块名以 扩展名.py 结尾.在模块内部,
# 模块名 (一个字符串) 可以通过一个全局变量 __name__取得.例如，用你最喜欢的文本编辑器
# 在当前目录下创建一个名为fibo.py的文件

def please(boy, action, girl):
    print(boy+" "+action+" to "+girl)

import math
print(math.pi)

import sys
print(sys.version)
print(sys.executable)

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把
# 这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，
# 因为__init__.py本身就是一个模块

# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，
# 自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

