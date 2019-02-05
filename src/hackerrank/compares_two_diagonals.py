import math

import os


def diagonal_difference(arr, n):
    first_diagonal = sum((arr[i][i]) for i in range(n))

    second_diagonal = sum((arr[n - i - 1][i]) for i in range(n))

    return int(math.fabs(first_diagonal - second_diagonal))


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()


def test():
    print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 3))


if __name__ == '__main__':
    test()
