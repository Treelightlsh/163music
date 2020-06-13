from timewrap import *
import random


def sift(li, low, high):
    """
    有一个堆，最顶端（省长）不是堆，其左右堆均是堆，现在要调整省长的位置
    :param li: 列表
    :param low: 堆的开始位置
    :param high: 堆的结束位置
    :return:
    """
    tmp = li[low]  # 堆顶端的值
    i = low  # 父亲的位置
    j = 2 * i + 1  # 左孩子的位置
    while j <= high:
        # 如果右孩子存在并且右孩子较大
        if j + 1 <= high and li[j + 1] > li[j]:
            # 把孩子当中较大的给j保存
            j += 1
        # 较大的孩子如果比省长大，则原省长位置就给此孩子
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


@call_time
def heap_sort(li):
    """
    对列表li利用堆进行排序，首先建堆，然后挨个数
    :param li:
    :return:
    """
    n = len(li)
    # 第一步、建堆
    for i in range(n // 2 - 1, -1, -1):
        sift(li, i, n - 1)
    # 第二步，挨个出数
    # j表示最后一个元素的位置
    for j in range(n - 1, -1, -1):
        # 交换省长和傀儡的位置，同时元素减1
        li[0], li[j] = li[j], li[0]
        sift(li, 0, j - 1)


li = list(range(10000))
random.shuffle(li)
heap_sort(li)
print(li)
