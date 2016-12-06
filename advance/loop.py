# 如果需要在循环内部去修改正在迭代的序列，可以使用切片来创建副本来达到目的
words = ['cat', 'window', 'defenestrate']
for word in words[:]:
    if len(word)>8:
        print(word)
        words.insert(0,word)
        print(words)

# 当你需要遍历一个数字序列的时候可以使用range(start,end,num)来生成一个等差数列
# 注意的是包括start，不包括end，num不填默认步长为1
for num in range(0,4,2):
    print(num)

# list(iterables)通过一个迭代器来创建一个list
print(list(range(4)))

# 找出10以内的质数
for num in range(2,11):
    for x in range(2,num):
        if num%x==0:
            print(num,"不是一个质数")
            break
    else:
        print(num,"是质数")
# for可以与else连用，这里的else需要遍历完这个循环才会进入

# pass语句什么都不做，起到这么几个作用：
# 1、用于在语法上必须要有一条语句的地方,如：
while True:
    pass
# 2、用于创建最小的类
class emptyClass:
    pass
# 3、用于编写逻辑时作为占位符