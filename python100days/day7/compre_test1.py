# 双色球选号


from random import randint, sample, randrange

def dispiay(balls):
    """

    :return: 输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' %ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return:
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        """
        在red_balls中随机选择6个不相同的数
        """
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # selected_balls = sample(red_balls, 6) # 在red_balls中随机选择6个不相同的数
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        dispiay(random_select())

if __name__ == '__main__':
    main()
