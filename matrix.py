def sum_up_diagonals(li):
    index = len(li)
    first_dia = sum(li[i][i] for i in range(index))
    second_dia = sum(li[i][index - i - 1] for i in range(index))
    abs_differ = abs(first_dia - second_dia)
    return abs_differ


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = sum_up_diagonals(arr)
    print(result)
