def simple_array_sum(ar):
    res = 0
    for el in ar:
        res += el
    return res


if __name__ == '__main__':

    ar_count = 6

    ar = [1, 2, 3, 4, 10, 11]

    result = simple_array_sum(ar)

    print(result)
