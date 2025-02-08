"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 arr_m 和 arr_n。
请你找出并返回这两个正序数组的中位数。
算法的时间复杂度应该为 O(log (m+n))。
"""
import random

len_m = random.randint(1, 100)
arr_m = [random.randint(0, 1000) for _ in range(len_m)]
arr_m.sort()
