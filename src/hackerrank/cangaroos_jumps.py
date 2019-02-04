def kangaroo(x1, v1, x2, v2):
    if x1 < x2:
        if v1 <= v2:
            return f'NO'
        else:
            while x1 < x2:
                x1 = x1 + v1
                x2 = x2 + v2
                if x1 == x2: return f"YES"
            if x2 > x1: return f"NO"
    elif x2 < x1:
        if v2 <= v1:
            return f'NO'
        else:
            while x2 < x1:
                x1 = x1 + v1
                x2 = x2 + v2
                if x1 == x2: return f"YES"
            if x1 > x2: return f"NO"
    else:
        if v1 == v2 and x1 == x2:
            return f"YES"
        else:
            return f"NO"


if __name__ == '__main__':
    print(kangaroo(0, 2, 5, 3))
