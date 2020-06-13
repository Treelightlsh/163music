import random
from timewrap import *


def partition(li, left, right):
    """
    此函数用于对于列表li，首先从一个随机位置和第一个位置交换数值，然后把第一个数放到一个位置，此位置的左边
    数值均比它小，右边的数值均比它大，返回此位置的索引
    :param li: 列表
    :param left: 最左边的位置
    :param right: 最右边的位置
    :return: 返回此位置的索引
    """
    # 交换数
    random_index = random.randint(left + 1, right)
    li[left], li[random_index] = li[random_index], li[left]
    tmp = li[left]
    while left < right:
        # 当left=right时，即找到位置时，退出循环
        while left < right and li[right] >= tmp:
            # 当找到比tmp小的数时退出循环
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            # 当找到比tmp大的数时退出循环
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def _quick_sort(li, left, right):
    if left < right:
        # 表明有起码有两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@call_time
def quick_sort(li):
    return _quick_sort(li, 0, len(li) - 1)


l = list(range(10000))
random.shuffle(l)
quick_sort(l)
print(l)
