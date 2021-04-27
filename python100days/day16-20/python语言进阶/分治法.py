"""
快速排序 - 选择轴对元素进行划分，左边都比轴小，右边都比轴大
"""
def quick_sort(items, comp=lambda x, y: x < y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items)-1, comp)
    return items

def _quick_sort(items, start, end , comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    i = start
    for j in range(start, end):
        if comp(items[j], items[end]):
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[end] = items[end], items[i]
    print(i)
    return i

items = [33, 23, 42, 42, 34, 2, 3, 4, 24, 243, 5, 2, 34, 5 , 34]
print(quick_sort(items))