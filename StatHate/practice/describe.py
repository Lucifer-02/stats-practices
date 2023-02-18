import math


def desc_unbiased_std(ls: list) -> float:
    sum = 0
    mean = desc_mean(ls)
    for i in ls:
        sum += (i - mean)**2

    return math.sqrt(sum/(len(ls) - 1))


def desc_biased_std(ls: list) -> float:
    sum = 0
    mean = desc_mean(ls)
    for i in ls:
        sum += (i - mean)**2

    return math.sqrt(sum/len(ls))


def desc_biased_var(ls: list) -> float:
    sum = 0
    mean = desc_mean(ls)
    for i in ls:
        sum += (i - mean)**2

    return sum/len(ls)


def desc_unbiased_var(ls: list) -> float:
    sum = 0
    mean = desc_mean(ls)
    for i in ls:
        sum += (i - mean)**2

    return sum/(len(ls) - 1)


def desc_mean(ls: list):
    s = 0
    for ele in ls:
        s += ele
    return s/(len(ls))


def desc_median(ls: list):
    ls.sort()
    length = len(ls)
    mid_id = int(length / 2)
    if (length % 2 == 0):
        return (ls[mid_id] + ls[mid_id-1])/2
    else:
        return ls[mid_id]


def desc_distinct(ls: list) -> list:
    length = int(len(ls))
    distinct = [ls[0]]
    for i in range(length - 1):
        if (ls[i] == ls[i+1]):
            continue
        else:
            distinct.append(ls[i+1])
    return distinct


def desc_ls_max(ls: list) -> float:
    max_val = ls[0]
    for ele in ls:
        if (max_val < ele):
            max_val = ele
    return max_val


def desc_mode(ls: list) -> list:
    modes = _most_occurs(ls)
    return modes[0]


def _most_occurs(ls: list) -> list:
    ls.sort()
    dist = desc_distinct(ls)
    counts = []
    for ele in dist:
        occur = 0
        for i in ls:
            if (ele == i):
                occur += 1
        counts.append(occur)

    most_occur = desc_ls_max(counts)

    modes = []
    for i in range(int(len(counts))):
        if (counts[i] == most_occur):
            modes.append(dist[i])

    return modes


def desc_range(ls: list) -> float:
    ls.sort()
    return (ls[-1] - ls[0])


def desc_inc_range(ls: list) -> float:
    ls.sort()
    return (ls[-1] - ls[0] + 1)


def print_mean(mean: float):
    print("Mean: ", mean)


def print_median(median: float):
    print("Median: ", median)


def print_mode(mode: float):
    print("Mode: ", mode)


def print_range(rg: float):
    print("Range: ", rg)
