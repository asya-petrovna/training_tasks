def count_apples_and_oranges(s, t, a, b, apples, oranges):
    home = range(s, t+1)
    apple_in_home = sum([1 if a + apple in home else 0 for apple in apples])
    orange_in_home = sum([1 if b + orange in home else 0 for orange in oranges])
    print(f'{apple_in_home} \n{orange_in_home}')


def test():
        return count_apples_and_oranges(7, 11, 0, 15, [2, 5, 7], [5, -5])


if __name__ == '__main__':
        test()


