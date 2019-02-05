def birthday_cake_candles(ar):
    biggest_value = max(ar)
    kolv = 0
    for i in range(len(ar)):
        if ar[i] >= biggest_value: kolv = kolv + 1
    return kolv


def test():
    print(birthday_cake_candles([3, 1, 2, 3]))


if __name__ == '__main__':
    test()

# def imput_data():
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    ar_count = int(input())

#    ar = list(map(int, input().rstrip().split()))

#    result = birthdayCakeCandles(ar)

#    fptr.write(str(result) + '\n')

#    fptr.close()
