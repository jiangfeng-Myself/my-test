from enum import Enum, unique # 枚举类型
from math import sqrt
from random import randint

import pygame

@unique # 检测枚举类型中是否有重复
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        return (r, g, b)

class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color = Color.RED):
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self._x += self._sx
        self._y += self._sy
        if self._x - self._radius <= 0 or self._x + self._radius >= screen.get_width():
            self._sx = - self._sx
        if self._y - self._radius <= 0 or self._y + self._radius >= screen.get_height():
            self._sy = - self._sy

    def eat(self, other):
        """大球吃小球"""
        if self.alive and other.alive and self != other:
            dx, dy = self._x - other._x, self._y - other._y
            distance = sqrt(dx**2 + dy**2)
            if distance < self._radius + other._radius and self._radius > other._radius:
                other.alive = False
                self._radius = self._radius + int(other._radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._radius, 0)



def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用语显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    print(screen.get_width())
    print(screen.get_height())
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 60
    runing = True
    # 开启一个事件循环处理发生的事件
    while runing:
        # 从消息列表中获取事件并进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-1, 1), randint(-1, 1)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255,255,255)) # 屏幕的背景颜色
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(10)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()


