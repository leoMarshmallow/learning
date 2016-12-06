# 斐波那契数列
a,b = 0,1
max = int(input("请输入一个大于1的整数"))
print(max)
while max<=0:
    print("长度至少为2，请从新设置")
    max = int(input("请输入一个大于1的整数"))
print(a)
while b<=max:
    print(b)
    a,b = b,a+b

# 循环体中都使用缩进，简洁的多个赋值，
# print("aaa",end='0')
# end=表示以*为结尾
# 因为 ** 的优先级高于 -， -3**2会被解释为 -(3**2) 并得到结果 -9.。
# 为了避免这一点并得到结果 9， 你可以使用 (-3)**2。
