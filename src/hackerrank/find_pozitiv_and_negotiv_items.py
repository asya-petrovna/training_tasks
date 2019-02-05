import math


def plusMinus(arr, kolv):
    poz, neg, zer = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] > 0:
            poz = (poz + 1)
        elif arr[i] < 0:
            neg = (neg + 1)
        else:
            zer = (zer + 1)
    a = poz / kolv
    b = neg / kolv
    c = zer / kolv
    strings = [a, b, c]
    print(*strings, sep='\n')


def main():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)


def test():
    return (plusMinus([-4, 3, -9, 0, 4, 1], 6))


if __name__ == '__main__':
    test()
