# 闭包的构成条件

# 定义闭包的语法格式

# 1.闭包的定义
# 在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称为闭包.

# 2.闭包的构成条件

# 1. 在函数嵌套(函数里面再定义函数)的前提下
# 2.内部函数使用了外部函数的变量(还包括外部函数的参数)
# 3.外部函数返回了内部函数

# demo

# 定义一个外部函数

def func_out(num1):
    # 定义一个内部函数

    def func_inner(num2):

        result = num1 + num2
        print("结果是:",result)

    # 外部函数返回了内部函数,这里返回的内部函数就是闭包

    return func_inner


f = func_out(5)

print(func_out)
print(f)
print(f(2))
print(f(3))

print("sss")
print(id(f))
print(id(f(2)))
print(id(f(3)))


# 4.闭包的作用
# 闭包可以保存外部函数内的变量,不会随着外部函数调用完而销毁.
# 由于闭包引用了外部函数的变量,则外部函数的变量没有及时释放

# 5.小结
#   1.当返回的内部函数使用了外部函数的变量就形成了闭包
#   2.闭包可以对外部函数的变量进行保存
#   3.实现闭包的标准格式

