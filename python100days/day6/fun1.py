
# 求阶乘的功能 函数

def factorial(n):
    result = 1
    for num in range(1,n + 1):
        result *= num
    return result

print(factorial(7)//factorial(3)//factorial(4))