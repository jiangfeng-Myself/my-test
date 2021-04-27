"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
"""

import sys
import time

SIZE = 5
total = 0

def print_board(board):
    for row in board:
        for col in board:
            print(str(col).center(4), end='')
        print()