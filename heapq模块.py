import heapq


def heap_sort(li):
    """
    利用heapq模块实现排序功能
    :param li:
    :return:
    """
    # 构造堆
    heapq.heapify(li)
    n = len(li)
    new_li = []
    for i in range(n):
        # heapop每次会从列表获取最小的值
        new_li.append(heapq.heappop(li))
    return new_li


li = [6, 8, 1, 9, 3, 0, 7, 2, 4, 5]
new_li = heap_sort(li)
print(new_li)
