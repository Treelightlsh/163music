import random


def bubble_sort(li):
    """
    冒泡排序
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        # i表示的是第几趟
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def bubble_sort2(li):
    """
    冒泡排序改进版，就是一趟没有任何改变，则直接结束
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        # i表示的是第几趟
        change = False
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                change = True
        if not change:
            return


li = list(range(0, 10000))
# random.shuffle(li)
bubble_sort2(li)
print(li)
