# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
import os


def divisibleSumPairs(n, k, ar):
    num_of_pairs = 0
    for index, i in enumerate(ar):
        for idx, j in enumerate(ar[index + 1:]):
            if index < len(ar) - 1:
                if (i + j) % k == 0:
                    num_of_pairs += 1
    return print(num_of_pairs)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

