def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0

    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        elif i == 0:
            zeros += 1
    ratios_positive = f'{positive / n:.6f}'
    ratios_negative = f'{negative / n:.6f}'
    ratios_zeros = f'{zeros / n:.6f}'

    return print(f'{ratios_positive}\n{ratios_negative}\n{ratios_zeros}')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
