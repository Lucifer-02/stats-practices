scores = [93,85,99,77,94,99,86,76,95,99,97,84,91,89,77,87,97,83,80,98,75,94,81,85,78,92,89,94,76,94,96,94,90,79,80,92,77,86,83,81]

# by hand
def mean(ls: list):
    s = 0
    for ele in ls:
       s += ele
    return s/(len(ls))

def median(ls: list):
    ls.sort()
    length = len(ls)
    mid_id = int(length / 2)
    if(length % 2 == 0):
        return (scores[mid_id] + scores[mid_id-1])/2
    else:
        return scores[mid_id]

def distinct(ls: list) -> list:
    length = len(ls)
    distinct = [ls[0]]
    for i in range(length - 1):
        if(ls[i] == ls[i+1]):
            continue
        else:
            distinct.append(ls[i+1])
    return distinct

def ls_max(ls: list) -> int:
    max_val = ls[0]
    for ele in ls:
        if(max_val < ele):
            max_val = ele
    return max_val
    
def mode(ls: list) -> list:
    ls.sort()
    dist = distinct(ls)
    counts = []
    for ele in dist:
        occur = 0
        for i in ls:
            if(ele == i):
                occur += 1
        counts.append(occur)

    most_occur = ls_max(counts)

    modes = []
    for i in range(len(counts)):
        if(counts[i] == most_occur):
            modes.append(dist[i])

    return modes
            


# use lib
import numpy as np
from scipy import stats as st

sc = np.array(scores)


def main():
    print("by hand:")
    print(mean(scores))
    print(median(scores))
    print(mode(scores))

    print("use lib:")
    print(np.mean(sc))
    print(np.median(sc))
    print(st.mode(sc, axis= None, keepdims=False))

if __name__ == "__main__":
    main()

