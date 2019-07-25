"""
1. 下标索引
    下标即编号，序号。
2.字符串中切片的使用：
    字符串实际就是字符的数组
"""

# 如果想取出部分字符，可以通过下标的方法：

name = "abcdefg"

print(name[0])
print(name[2])
print(name[3])

"""
1. 切片
    切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作
2. 切片的语法
    [起始：结束：步长]
    选取的区间从起始开始，到结束前的前一位结束（不包含结束位本身），步长表示选取间隔
     
"""

print(name[0:3])
print(name[0:5])
print(name[3:5])
print(name[1:10])
print(name[0:])
print(name[0:-1]) # 从下标为0开始 到最后第一个之前的字符
print(name[-1:])  #从倒数最后一个到最后一个之间的字符
print(name[::-1])

# 练一练

s = 'Hello World!'

print(s[4])

print(s)

print(s[:]) # 取出所有元素（没有起始位和结束位之分），默认步长为1

print(s[1:]) # 从下标为1开始，取出 后面所有的元素（没有结束位）

print(s[:5])  # 从起始位置开始，取到 下标为5的前一个元素（不包括结束位本身）

print(s[:-1]) # 从起始位置开始，取到 倒数第一个元素（不包括结束位本身）

print(s[-4:-1]) # 从倒数第4个元素开始，取到 倒数第1个元素（不包括结束位本身）

print(s[1:5:2]) # 从下标为1开始，取到下标为5的前一个元素，步长为2（不包括结束位本身）

# python 字符串快速逆置

print(s[::-1])  # 从后向前，按步长为1进行取值