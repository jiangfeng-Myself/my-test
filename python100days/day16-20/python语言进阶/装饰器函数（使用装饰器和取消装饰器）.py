from functools import wraps
from time import time


def record_time(func):
    """自定义装饰器函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result

    return wrapper

