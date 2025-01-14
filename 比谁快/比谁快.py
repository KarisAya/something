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
