"""
作用域问题
"""

# 局部作用域
def foo1():
    a = 5

foo1()

# 全局作用域
b = 10

def foo2():
    print(b)

foo2()

def foo3():
    b = 100
    print(b)

foo3()
print(b)

def foo4():
    global  b
    b = 200
    print(b)

foo4()
print(b)

a, b = 5, 10
print(f'{a} * {b} = {a * b}')
print('{0} * {1} = {2}'.format(a,b,a*b))