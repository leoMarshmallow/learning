print('hi, %s, you have $%d.' % ('michael', 1000000))
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
# 后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略.

print('%.2f   %d' % (3.1415926, 1))
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

# list用[]定义,tuple元组用()定义
# 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改,代码更安全
# t=(1)定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
# 因此，python规定，这种情况下，按小括号进行计算，计算结果自然是1。所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义

# dict类似于map,在python中叫做数据字典,dict内部存放的顺序和key放入的顺序是没有关系的。

# if-elif-else