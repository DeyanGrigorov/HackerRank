def birthdayCakeCandles(candles):
    biggest_candle = 0
    count = 0
    for i in candles:
        if i > biggest_candle:
            biggest_candle = i
    for i in candles:
        if i == biggest_candle:
            count += 1
    return count


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
