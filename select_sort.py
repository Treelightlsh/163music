import random


def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i  # 最小数位置
        for j in range(i + 1, len(li) - 1):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


li = list(range(10000))
random.shuffle(li)
select_sort(li)
print(li)
