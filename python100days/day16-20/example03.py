"""
函数递归调用-函数直接或间接的调用了自身
1，收敛条件
2，递归公式

n! = n * (n-1)!
f(n) = f(n-1) * f(n-2)
1,1,2,3,5,8,13,21,34,55...
"""
from contextlib import contextmanager
from time import perf_counter

def fac(num):
    """求阶乘"""
    assert num >= 0
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

def fib2(num):
    """普通员工"""
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return a

def fib3(num):
    """生成器"""
    a, b  = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a

def fib(num, results={}):
    """斐波那契数"""
    assert num > 0
    if num in (1, 2):
        return 1
    try:
        return results[num]
    except KeyError:
        results[num] = fib(num - 1) + fib(num - 2)
        results results[num]

@contextmanager
def timer():
    try:
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}秒')

def main():
    """主函数"""