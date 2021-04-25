"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
"""

# 参数默认值
def f1(a, b = 5, c = 10 ):
    return a + b * 2 + c * 3

print(f1(1,2,3))
print(f1(100, 100))
print(f1(100))
print(f1(c= 3,a = 3, b =3))

# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1,2,3))
print(f2(1,2,3,4,5))
print(f2())

# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是：%s!' % kw['tel'])
    else:
        print('没有找到你的个人信息！')

parms = {'name': '江枫', 'tel': 28}
f3(**parms)
f3(name = '江枫', age = 38, tel= '173348234')
f3(user = '江枫', age = 38, tel= '173348234')
f3(user = '江枫', age = 38, mobile= '173348234')