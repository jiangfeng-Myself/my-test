"""
子列表元素之和的最大值
"""

def main():
    items = list(map(int, input('输入一串数：').split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)

if __name__ == '__main__':
    main()
