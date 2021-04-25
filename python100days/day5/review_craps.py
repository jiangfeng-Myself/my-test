from random import randint

money = 1000
while True:
    print('你的总资产为：%d'%money)
    need_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点'%first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        need_go_on = True

    while need_go_on:
        second = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % second)
        if second == 7:
            print('庄家胜')
            money -= debt
            need_go_on = False
        elif second == first:
            print('玩家胜')
            money += debt
            need_go_on = False

