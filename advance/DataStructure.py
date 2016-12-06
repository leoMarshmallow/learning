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