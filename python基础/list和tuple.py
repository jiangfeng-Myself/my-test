# list(列表):
arr = ['a', 'b', 'c']
print(arr)
print(len(arr))  # 列表的长度
print(arr[2])  # 通过下标索引查询数据
print(arr[-1])  # 倒序索引查询数据
arr.append('d')  # 在列表末尾插入数据
print(arr)
arr.insert(1, 'e')  # 通过下标索引来插入数据
print(arr)
arr.pop()  # 删除最后一个数据
print(arr)
arr.pop(1)  # 通过索引删除数据
print(arr)
arr[2] = 'g'  # 通过索引替换当前索引的元素
print(arr)
# list中可以有不同数据类型的元素 eg：
arr2 = ['a', 123, True]
print(arr2)
# list里可以包含另一个list
arr3 = ['a', 'b', ['c', 'd'], 'e']
print(arr3[2][1])  # d
# tuple(元祖)：
# tuple一旦被定义就不能被改变值 eg：
Trr = (1, 2, 3)
print(Trr)
Trr2 = ()  # 空的tuple
Trr3 = (1,)  # 只有一个元素的tuple
