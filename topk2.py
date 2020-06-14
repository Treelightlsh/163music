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


def top(li, k):
    """
    得出列表中前k个的值
    :param li:
    :param k:
    :return:
    """
    heap = li[0:k]
    # 首先创建堆
    for i in range(k // 2 - 1, -1, -1):
        sift(heap, i, k - 1)
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


import random

li = [2, 9, 8, 6, 5, 4, 3]
sift(li, 0, len(li) - 1)
print(li)
