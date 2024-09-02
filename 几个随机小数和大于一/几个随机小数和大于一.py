# 计算结果 2.7178742 计算耗时 5.331498622894287 秒
import random
import time

LOOP: int = 10000000

random.seed(time.time())
start = time.time()
n = 0
for _ in range(LOOP):
    x = 0.0
    while x < 1:
        x += random.uniform(0.0, 1.0)
        n += 1
end = time.time()

print(f"计算结果 {n/LOOP} 计算耗时 {end - start} 秒")
