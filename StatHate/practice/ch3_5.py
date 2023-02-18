import ch2_1


def std(var: float) -> float:
    return pow(var, 0.5)


def biased_var(ls: list, mean: float) -> float:
    sum = 0
    for i in ls:
        sum += (i - mean)**2

    return sum/len(ls)


def unbiased_var(ls: list, mean: float) -> float:
    sum = 0
    for i in ls:
        sum += (i - mean)**2

    return sum/(len(ls) - 1)


def main():
    scores = [94, 86, 72, 69, 93, 79, 55, 88, 70, 93]

    scores.sort()

    print("Range: ", scores[-1] - scores[0])

    mean = ch2_1.mean(scores)
    print("Phương sai không thiên vị: ", unbiased_var(scores, mean))
    print("Phương sai thiên vị: ", biased_var(scores, mean))
    print("Độ lệch chuẩn không thiên vị: ", std(unbiased_var(scores, mean)))
    print("Độ lệch chuẩn thiên vị: ", std(biased_var(scores, mean)))


if __name__ == "__main__":
    main()
