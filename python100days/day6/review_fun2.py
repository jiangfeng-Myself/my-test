"""
函数的定义和使用 - 求最大公约数和最小公倍数
"""

def gcd(x, y):
    if x > y:
        x, y = y, x
    for fac in range(x, 1, -1):
        if x % fac == 0 and y % fac == 0:
            return  fac
    return 1

def lac(x, y):
    return x * y // gcd(x, y)