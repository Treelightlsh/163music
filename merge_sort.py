def merge(li, low, mid, high):
    """
    一次归并
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    i = low
    j = mid + 1
    l_tmp = []
    # 左右两边的指针都还未遍历完时
    while i <= mid and j <= high:
        if li[i] < li[j]:
            l_tmp.append(li[i])
            i += 1
        else:
            l_tmp.append(li[j])
            j += 1
    while i <= mid:
        l_tmp.append(li[i])
        i += 1
    while j <= high:
        l_tmp.append(li[j])
        j += 1
    li[low:high+1] = l_tmp


def _merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


import random
li = list(range(16))
random.shuffle(li)
print(li)
_merge_sort(li, 0, len(li)-1)
print(li)
