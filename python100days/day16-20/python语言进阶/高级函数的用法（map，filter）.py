def main():
    items = [23,34,32,43,432,23,4,5,34,34]
    items1 = list(map(lambda x:x ** 2, filter(lambda x:x%2, items)))
    print(items1)
    items2 = [x ** 2 for x in items if x % 2 ]
    print(items2)


if __name__ == '__main__':
    main()