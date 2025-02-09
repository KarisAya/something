"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 arr_m 和 arr_n。
请你找出并返回这两个正序数组的中位数。
算法的时间复杂度应该为 O(log (m+n))。
"""

import random
import numpy as np

count = 0


def find(arr_x: list[int], arr_y: list[int], n: int):
    """寻找两个数组从小到大第n个数 n 从 0 开始"""
    global count
    while True:
        count += 1
        if not arr_x:
            return arr_y[n]
        if not arr_y:
            return arr_x[n]
        if n == 0:
            return min(arr_x[0], arr_y[0])
        len_x = len(arr_x)
        len_y = len(arr_y)
        # arr_x 是较短的数组
        if len_x > len_y:
            len_x, len_y = len_y, len_x
            arr_x, arr_y = arr_y, arr_x
        cut_x = n - n // 2
        if cut_x > len_x:
            cut_x = len_x
        # 让长数组数组偏移量略大
        cut_y = n - cut_x + 1
        # 偏移量 - 1
        if arr_x[cut_x - 1] < arr_y[cut_y - 1]:
            arr_x = arr_x[cut_x:]
            n -= cut_x
        else:
            arr_y = arr_y[cut_y:]
            n -= cut_y


def find_median(arr_x: list[int], arr_y: list[int]):
    len_tot = len(arr_x) + len(arr_y)
    harf = len_tot // 2
    if len_tot % 2 == 0:
        left = find(arr_x, arr_y, harf - 1)
        right = find(arr_x, arr_y, harf)
        global count
        count /= 2
        # 我宣布常数时间耗时翻倍，于是循环次数 /2

        return (left + right) / 2
    else:
        return find(arr_x, arr_y, harf)


len_m = random.randint(1, 100)
len_n = random.randint(1, 100)
arr_m = [random.randint(0, 1000) for _ in range(len_m)]
arr_n = [random.randint(0, 1000) for _ in range(len_n)]
arr_m.sort()
arr_n.sort()

print(f"{find_median(arr_m,arr_n) = }")
print(f"{np.median(np.array(arr_m+arr_n)) = }")
print(f"O(log(m+n)) = {np.log2(len_m+len_n)}")
print(f"循环次数：{count = }")
