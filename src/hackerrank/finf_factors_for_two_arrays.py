def get_factors(first_m, second_m):
    third_m = []
    for i in first_m:
        for j in second_m:
            if int(first_m[i] % second_m[j]) == first_m[i] % second_m[j]:
                third_m.append(first_m[i] % second_m[j])
    return third_m


def getTotalX(a, b):
    mass = get_factors((range(b[0], a[len(a) - 1])), a)
    mass2 = get_factors(b, mass)
    return len(mass2)


if __name__ == '__main__':
    print(getTotalX((2, 4), (16, 32, 96)))
