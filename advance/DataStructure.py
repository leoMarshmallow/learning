# =========列表============
# 列表的扩展
# pop([i])（i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。

l = [0, 1, 2]

# 追加到列表末尾，相当于l[len(l):]=[x]
l.append(3)
print(l)

# 将另一个list追加到一个list后，相当于 l[len(l):] = L2
l.extend([8,9])
print(l)

# 插入
l.insert(1,9)
print(l)

# 删除列表中首次出现的元素，如果没有则报错
l.remove(9)
print(l)

# 根据下标去删除列表中的元素
del l[0]
print(l)
del l[3:]
print(l)
# del l 删除变量

# 弹出列表中的元素,如果没有参数则默认弹出最后一个
print(l.pop())
print(l.pop(1))

# 清除列表中所有元素
# l.clear()

# 获取列表中元素的首次出现的下标
l.append(0)
print(l.index(0))

# 获取列表中某元素出现的次数
print(l.count(0))

# 将列表排序,key=none则默认直接比较元素
l.extend([9,8])
l.sort(key=None,reverse=False)
print(l)

# 位置的反转
l.reverse()

# 返回这个列表的浅拷贝。相当于 a[:]
print(l.copy())

# ===============================
# 列表在队列中的使用
from collections import deque
queue = deque(["xyc","sz","leo"])
queue.append("tom")
queue.append("jerry")
print(queue)
print(queue.popleft())
print(queue.popleft())

# ==========列表推导式============
# 列表推导式由一对方括号组成，方括号包含一个表达式，其后跟随一个for子句，然后是零个
# 或多个for或if子句。结果将是一个新的列表，其值来自将表达式在其后的for和if子句的上下文
# 中求值得到的结果。例如：
lb = [x+y for x in [1,2,3] for y in [3,4,2] if x != y]
print(lb)
# 也可以在表达式中使用函数，如：
print([abs(x) for x in [-1,-9,3,5]])
# 当然也可以在表达式中嵌套另一个列表推导式，先外层再里层，如：
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
# zip()可以实现行列互换
print(list(zip(*matrix)))

# =========元祖============
# 元组由逗号分割的若干值组成，例如：
t = "aa", "bb", "cc"
print(t,t[0])

# 一个特殊的问题是构造包含0个或1个元素的元组：为了实现这种情况，语法上有一些奇怪。
# 空的元组通过一对空的圆括号构造；只有一个元素的元组通过一个元素跟随一个逗号构造
# （仅用圆括号把一个值括起来是不够的）
empty = ()

# 这被称为序列分拆再恰当不过了，且可以用于右边的任何序列。序列分拆要求等号左侧的变量和
# 序列中的元素的数目相同。注意多重赋值只是同时进行元组封装和序列分拆。
x, y, z = t
print(x,y,z)

# =========集合============
# 集合中的元素不会重复且没有顺序。集合的基本用途包括成员测试和消除重复条目。
# 集合对象还支持并集、 交集、 差和对称差等数学运算。
# 花括号或者set()函数可以用来创建集合。注意，你必须使用set()创建一个空的集合，
# 而不能用{}；后面这种写法创建一个空的字典.
fruits = {"apple", "pear", "orange"}
print(fruits,"apple" in fruits)

apple = set("apple")
orange = set("orange")
print(apple,orange,apple-orange)

# 同样也支持推导式
print({x for x in "asdasccdasd" if x not in "asd"})

# =========字典============
# 字典的键可以是任意不可变的类型，键必须是唯一的
singer = {"jj" : 99, "jay": 100, "ed sheeran" : 99}
print(sorted(singer.keys()),singer["jj"],"leehom" in singer)

# 字典也可以通过推导式获得
print({x : x**2 for x in [2,3,4]})

# 可以通过dict()构造函数来构建字典
print(dict(a=1,b=2,z=26))

# ==========循环技巧===========
# 需要循环遍历字典时，可以用items提取出来，如：
for k, v in singer.items():
     print(k + "---->" + v.__str__())

# 当遍历一个序列时，使用enumerate()函数可以同时得到位置索引和对应的值。
for i, v in enumerate(["jj", "jay", "leehom"]):
     print(i,v)

# 同时遍历两个或更多的序列，使用zip()函数可以成对读取元素。
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

# 反向遍历序列
for i in reversed([2,3,4]):
     print(i)

for i in sorted([2,3,1,2]):
     print(i)

# is,is not 判断是否为同一个对象
# 所有比较运算符都具有相同的优先级，低于所有数值运算符。
# 可以级联比较。例如，a < b == c测试a是否小于b并且b是否等于c。

# 可以使用布尔运算符and和or组合，比较的结果（或任何其他的布尔表达式）可以用not取反。
# 这些操作符的优先级又低于比较操作符；它们之间，not 优先级最高，or 优先级最低，所以
# A and not B or C 等效于 (A and (not B)) or C。与往常一样，可以使用括号来表示
# 所需的组合。

# 布尔运算符and 和 or 是所谓的 短路 运算符：依参数从左向右求值，结果一旦确定就停止。
# 例如，如果A 和 C 都为真，但B是假， A and B and C 将不计算表达式 C。当用作一个普通
# 值而非逻辑值时，短路操作符的返回值通常是最后一个计算的。
