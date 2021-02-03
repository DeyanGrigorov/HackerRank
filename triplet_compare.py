import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for index, value in enumerate(a):
        if value > b[index]:
            a_points += 1
        elif value < b[index]:
            b_points += 1
    return print(a_points, b_points)



if __name__ == "__main__":

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)


