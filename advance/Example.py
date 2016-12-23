#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a format example'
# 此行为注释

__author__='leo'
# 作者

import sys
# 引用模块

def fun():
    args = sys.argv
    if len(args)==1:
        print("==!")
    elif len(args)==2:
        print("=.=")
    else:
        print("...")

if __name__ == '__main__':
    fun()

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个
# 参数永远是该.py文件的名称，例如：运行python3 hello.py获得的sys.argv就是['hello.py']；
# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。