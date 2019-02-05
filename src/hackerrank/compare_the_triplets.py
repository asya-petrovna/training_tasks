#!/bin/python3


# Complete the compareTriplets function below.
def compare_triplets(a, b):
    v, p = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            v = v + 1
        elif a[i] < b[i]:
            p = p + 1

    return [v, p]


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    alice = list(map(int, input().rstrip().split()))

    bob = list(map(int, input().rstrip().split()))

    result = compare_triplets(alice, bob)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


def test():
    print(compare_triplets([5, 6, 7], [3, 6, 10]))


if __name__ == '__main__':
    test()
