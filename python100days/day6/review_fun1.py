# 求阶乘的函数

def factorial(n):
    result = 1
    for num in range(1,n + 1):
        result *= num
    return result

print(factorial(4))