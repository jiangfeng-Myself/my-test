"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

"""

def myfileter(mystr):
    return len(mystr) == 6

print(chr(0x9a86))
print(hex(ord('骆')))
print(abs(-1.2345)) # 绝对值
print(round(-1.2345)) # 取整
print(pow(1.2345, 5)) # 1.2345的5次方值

fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)]) # 切片
fruits2 = [list(filter(myfileter, fruits))]
print(fruits)
print(fruits2)