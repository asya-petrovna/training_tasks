def staircase(num_stairs):
    for stairs in range(1, num_stairs + 1):
        print(' ' * (num_stairs - stairs) + '#' * stairs)


if __name__ == '__main__':
    staircase(6)
