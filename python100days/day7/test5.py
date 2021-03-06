def is_leap_year(year):
    """
    判断指定年份是不是闰年
    :param year: 年份
    :return: 闰年返回True 不是返回False
    """
    return year % 4 == 0 and year % 100 == 0 and year % 400 == 0

def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    day_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
    total = 0
    for index in range(month - 1 ):
        total +=  day_of_month[index]
    return total + date

def main():
    print(which_day(1980, 11, 28))

if __name__ == '__main__':
    main()