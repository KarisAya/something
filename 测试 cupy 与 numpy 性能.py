"""
n = 10000000
numpy 进行浮点运算：耗时0.009500265121459961
cupy 进行浮点运算：耗时0.009999752044677734

n = 1000000000

numpy 进行浮点运算：耗时0.929999828338623
cupy 进行浮点运算：耗时0.1634998321533203
"""

import cupy as cp
import numpy as np
import time

n = 10000000


int_list = [1 for _ in range(n)]

start = time.time()
sum(int_list)
end = time.time()
print(f"python 进行整数运算：耗时{end - start}")

float_list = [1.0 for _ in range(n)]

start = time.time()
sum(float_list)
end = time.time()
print(f"python 进行浮点运算：耗时{end - start}")

np_int_list = np.array(int_list)

start = time.time()
np.sum(np_int_list)
end = time.time()
print(f"numpy 进行整数运算：耗时{end - start}")

np_float_list = np.array(float_list)

start = time.time()
np.sum(np_float_list)
end = time.time()
print(f"numpy 进行浮点运算：耗时{end - start}")

cp_int_list = cp.array(int_list)

start = time.time()
cp.sum(cp_int_list)
end = time.time()
print(f"cupy 进行整数运算：耗时{end - start}")

cp_float_list = cp.array(float_list)

start = time.time()
cp.sum(cp_float_list)
end = time.time()
print(f"cupy 进行浮点运算：耗时{end - start}")
