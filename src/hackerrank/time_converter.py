import time


def time_conversion(twelve_time):
    ptime = time.strptime(twelve_time, "%I:%M:%S%p")
    return time.strftime("%H:%M:%S", ptime)


if __name__ == '__main__':
    print(time_conversion('12:05:45AM'))

# cde
# abc

# cdecac
# abcc
