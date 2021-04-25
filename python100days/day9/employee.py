"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        :return: 月薪
        """
        pass

class Message(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""

    def __init__(self, name, work_hour = 0):
        super().__init__(name)
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self, work_hour):
        self._work_hour = work_hour if work_hour > 0 else 0

    def get_salary(self):
        return  self.work_hour * 150.0

class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales = 0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return  self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return self._sales * 0.05 + 1200

def main():
    emps = [
        Message('刘备'), Programmer('诸葛亮'),
        Message('曹操'), Salesman('葛勋'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer) : # isinstance() 判断两个参数类型是否相同
            emp.work_hour = int(input('请输入%s本月的工作时间：' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = int(input('请输入%s本月的销售额：' % emp.name))
        print('%s本月的工资为：￥%s元' % (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()