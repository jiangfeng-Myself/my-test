# for循环
# 计算1到10 的总和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 计算1到100的总和
# range 方法
print(list(range(1, 101)))
sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)
