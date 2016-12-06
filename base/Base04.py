#print(2**3)
# **表示乘方

#print(r"i'm \=./")
# r加字符串表示使用原始字符串

# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
# 通过""" """可以更灵活的排版

#print(3*"a"+2*"b")
## 可以通过*+来拼接字符串

#print("a""b")
# 两个引号相邻的字符串会自动拼接起来

# word = '你呢？'
# print(word[0])
# print(word[-1])
# print(word[0:2])
# print(word[1:])
# print(len(word))
# 字符串可以直接使用索引，为负数的索引都是从最右开始,而且支持灵活的切片
# word[0] = 'o'
# Python 字符串不能更改 — — 他们是 不可变的。因此，赋值给字符串索引的位置会导致错误

numbers = [1,2,3]
numbers+=[4,5]
numbers.append(6)
numbers[2:4]=['a']
print(numbers)
a = ['aaa',numbers]
print(a)