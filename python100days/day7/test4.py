def max2(x):
    """
    返回传入的列表中最大和第二大的元素的值
    :param x: 传入的数列
    :return: 返回最大和第二大的值
    """
    m1, m2 = (x[0], x[1]) if x[0]>x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

print(max2([2,3,5,23,64,23,42,5]))