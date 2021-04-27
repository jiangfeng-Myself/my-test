
def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序算法"""
    items = items[:]
    for i in range(len(items) - 1):
        mid_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[mid_index]):
                mid_index = j
        items[i], items[mid_index] = items[mid_index], items[i]
    return items