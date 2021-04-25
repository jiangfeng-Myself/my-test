from abc import  ABCMeta, abstractmethod
from random import randint

class Fighter(object, metaclass=ABCMeta):
    """战斗者"""


    # 通过__slots__魔法限定对象可以绑定的成员数量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other: 被攻击的对象
        :return:
        """
        pass

class U1traman(Fighter):
    """
    奥特曼
    """

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技（打掉对方至少50点或四分之三的血
        :param other: 被攻击的对象
        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param other: 被攻击的对象
        :return: 使用成功放回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False