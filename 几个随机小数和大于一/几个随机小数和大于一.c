// 计算结果 2.718054 计算耗时 0.490000 秒

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int LOOP = 10000000;
int main(void)
{
    srand(clock());
    double start = clock();
    int n = 0;
    for (int i = 0; i < LOOP; ++i)
        for (double x = 0.0; x < 1; x += (double)rand() / RAND_MAX)
            ++n;
    double end = clock();
    printf("计算结果 %.6f 计算耗时 %.6f 秒\n", (double)n / LOOP, (end - start) / CLOCKS_PER_SEC);
}