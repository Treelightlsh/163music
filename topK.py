import random


def sift(li, low, high):
    """
    对于小根堆，向下调整
    :param li:
    :param low:
    :param high:
    :return:
    """
    # 省长
    tmp = li[low]
    # 父亲的位置
    i = low
    # 左孩子的位置
    j = 2 * i + 1
    while j <= high:
        # j保存的是较小孩子的索引
        if j + 1 <= high and li[j + 1] < li[j]:
            j += 1
        # 较小的孩子比原省长小
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            # 省长找到位置
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
        sift(heap, 0, k - 1)
    for i in range(k, len(li)):
        if li[i] < heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


li = list(range(10000))
random.shuffle(li)
heap = top(li, 6)
print(heap)
