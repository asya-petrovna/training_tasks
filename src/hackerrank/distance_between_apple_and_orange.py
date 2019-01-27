def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apple_in_home, orange_in_home = 0, 0
    home = range(s, t+1)
    new_apples = [apples[i] + a for i in range(len(apples))]
    new_oranges = [oranges[k] + b for k in range(len(oranges))]
    for i in range(len(new_apples)):
        if new_apples[i] in home: apple_in_home = apple_in_home+1
    for k in range(len(new_oranges)):
        if new_oranges[k] in home: orange_in_home = orange_in_home +1
    print(f'{apple_in_home} \n{orange_in_home}')


def test():
        return count_apples_and_oranges(7, 11, 0, 15, [2, 5, 7], [5, -5])


if __name__ == '__main__':
        test()


