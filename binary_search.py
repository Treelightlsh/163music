def binary_search(li, val):
    """
    二分查找法
    :param li:
    :param val:
    :return:
    """
    low = 0
    height = len(li) - 1
    while low <= height:
        mid = (low + height) // 2
        if li[mid] > val:
            height = mid - 1
        elif li[mid] < val:
            low = mid + 1
        else:
            return mid
    else:
        return -1


li = range(0, 10000, 2)
print(binary_search(li, 367))
