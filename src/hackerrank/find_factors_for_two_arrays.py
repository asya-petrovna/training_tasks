def filter_factorizing(numbers_to_filter, check_numbers):
    result = []
    for candidate in numbers_to_filter:
        if all([max(candidate, jury) % min(candidate, jury) == 0 for jury in check_numbers]):
            result.append(candidate)
    return result


def getTotalX(a, b):
    range_to_check = range(max(a), min(b) + 1)
    filtered = filter_factorizing(range_to_check, a)
    filtered = filter_factorizing(filtered, b)
    return len(filtered)


if __name__ == '__main__':
    assert getTotalX([2, 4], [16, 32, 96]) == 3
    assert getTotalX([16, 32, 96], [2, 4]) == 0
    assert getTotalX([16, 32, 1], [2, 96]) == 0
    assert getTotalX([4, 2], [32, 96, 16]) == 3
    assert getTotalX([2, 4], [4]) == 1
    assert getTotalX([2, 4], [8]) == 2
    assert getTotalX([2, 2, 4], [8, 8]) == 2
    assert getTotalX([7], [7]) == 1
    assert getTotalX([2, 7], [8]) == 0
    print('Hooray!')
