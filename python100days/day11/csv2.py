"""
写入csv文件
"""

import csv

class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title

filename = 'teacher.csv'
teacher = [Teacher('江枫', 25, '叫兽'), Teacher('吴金柳', 24, '小笨蛋')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teacher:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('无法写入文件', filename)
else:
    print('保存数据完成')