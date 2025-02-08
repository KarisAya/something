"""
题目描述
狗爷和小猪正在进行摸鱼游戏。池塘中游动着n条鱼，它们排成了一条直线队列，其中有 m 条锦鲤
每条锦鲤的具体位置已知。狗爷和小猪将轮流进行操作，每一轮中，每人都必须选择并摸走队列开头或
者结尾的一条鱼，这个过程会一直持续，直到队列中仅剩下一条鱼。这时，如果唯一剩下的这条鱼是
条锦鲤，那么狗爷将获得胜利，否则邪恶的小猪将夺走锦鲤。每次游戏中，小猪将进行首次操作。可以
肯定的是，小猪和狗爷俩人都非常聪明，他们总会选择对自己最有利的策略进行游戏。请判定狗爷能否
取得游戏胜利。如果狗爷可以赢得胜利，输出 Goldye。否则，输出 Xiaozhu Hahaha。
输入格式
第一行输入两个正整数 n,m，分别代表鱼的总数和锦鲤的数量。
第二行输入 m 个整数，代表每条锦鲤在队列中的位置。位置编号从1到n。
输出格式
输出一行字符串。如果狗爷可以赢得胜利，输出 Goldye。否则，输出 Xiaozhu Hahaha。
"""

import random


def create_list(m, n):
    fish_list = [0 for _ in range(n)]
    for i in range(m):
        fish_list[i] = 1
    random.shuffle(fish_list)
    return fish_list


def action(fish_list: list):
    i_l = 0
    i_l_list = []
    for i in fish_list:
        i_l += 1
        if i == 1:
            i_l_list.append(i_l)

    l = len(fish_list)
    i_r_list = [l - x for x in i_l_list]
    i_r_list.reverse()
    return i_l_list, i_r_list


def xiaozhu_Action(i_l_list: list, i_r_list: list):
    n = len(i_l_list)
    for i in range(n):
        if i_l_list[i] < i_r_list[i]:
            return 0
        elif i_l_list[i] > i_r_list[i]:
            return -1
        else:
            pass
    return 0


def goldye_Action(i_l_list: list, i_r_list: list):
    n = len(i_l_list)
    for i in range(n):
        if i_l_list[i] > i_r_list[i]:
            return 0
        elif i_l_list[i] < i_r_list[i]:
            return -1
        else:
            pass

    return 0


def run(m: int, n: int):
    fish_list = create_list(m, n)
    while True:
        if len(fish_list) == 1:
            break
        fish_list.pop(xiaozhu_Action(*action(fish_list)))
        if len(fish_list) == 1:
            break
        fish_list.pop(goldye_Action(*action(fish_list)))

    return fish_list[0]


loop = 100
print(f"模拟次数: {loop}")
for n in range(5, 11):
    for m in range(n + 1):
        print(f"{m=},{n=} 狗爷胜率:", end="")
        print(sum(run(m, n) for _ in range(loop)) / loop)
