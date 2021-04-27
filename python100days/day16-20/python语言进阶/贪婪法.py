"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""

class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight

def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input('请输入物品名称、价格、重量：').split()
    return name_str, int(price_str), int(weight_str)

def main():
    """主函数"""
    max_weight, num_of_things = map(int, input('请输入最大重量和物品数量：').split())
    all_thing = []
    for _ in range(num_of_things):
        all_thing.append(Thing(*input_thing()))
    all_thing.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_thing:
        if total_weight + total_weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值：{total_price}美元')

if __name__ == '__main__':
    main()