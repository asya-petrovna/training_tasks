def mini_max_sum(origin):
    good_array = origin.copy()
    sum_array = []
    for i in range(5):
        work_array = good_array.copy()
        work_array.pop(i)
        sum_array.append(sum(work_array))
    return f'{min(sum_array)} {max(sum_array)}'


if __name__ == '__main__':
    print(mini_max_sum([1, 2, 3, 4, 5]))
