import random


def insert_sort(li):
    for i in range(1, len(li)):
        # 无序区的第一个数
        tmp = li[i]
        # 有序区的最后一个位置
        j = i - 1
        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = tmp


li = list(range(10000))
random.shuffle(li)
insert_sort(li)
print(li)
