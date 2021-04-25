# dict(字典)
a = {
    'a': 1,
    'b': 2,
    'c': 3,
}
print(a)
a['a'] = 4  # 修改字典中指定键的值
print(a)
print('a' in a)  # 判断‘a’是否在a中
a.get('d', -1)  # get()判断a中是否有‘a’这个key，没有则返回-1
a.pop('a')  # 删除‘a’这个键值对
print(a)
# set
s1 = set([1, 1, 2, 3, 3, 4])
print(s1)
s2 = set([1, 3, 2])
print(s2)
print(s1 & s2)
print(s1 | s2)
