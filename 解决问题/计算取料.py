"""
计算取料
一项工程需要管状材料若干
由于材料商店只成根出售，所以需要优化切割方式，使所需总材料尽可能小
未切割的材料长度6米，请计算需要的材料总总量和切割方式
"""

needs = []


def cut_materials(needs):
    """较长优先方案"""
    # 将需求按从大到小排序
    sorted_needs = sorted(needs, reverse=True)
    bins = []  # 存储每根原材料的切割情况及其剩余长度

    for length in sorted_needs:
        placed = False
        # 尝试将当前材料放入已有的原材料中
        for i in range(len(bins)):
            if bins[i]["remaining"] >= length:
                bins[i]["pieces"].append(length)
                bins[i]["remaining"] -= length
                placed = True
                break
        # 若无法放入，则创建新原材料
        if not placed:
            bins.append({"pieces": [length], "remaining": 6 - length})
    # 整理结果输出
    result = {"num_bins": len(bins), "cuts": [bin["pieces"] for bin in bins]}
    return result


result = cut_materials(needs)
print(f"需要 {result['num_bins']} 根")
for i, cut in enumerate(result["cuts"], 1):
    print(f"第{i}根切割: {cut} (总长度: {sum(cut)}米)")
