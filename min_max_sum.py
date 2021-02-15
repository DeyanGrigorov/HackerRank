def miniMaxSum(arr):
    four_max = arr.copy()
    four_min = arr.copy()
    four_min.remove(min(four_min))
    four_max.remove(max(four_max))
    four_max_res = sum(four_max)
    four_min_res = sum(four_min)
    return print(f'{four_max_res} {four_min_res}')


if __name__ == '__main__':
    arr = list(map(int, input().split()))

    miniMaxSum(arr)
