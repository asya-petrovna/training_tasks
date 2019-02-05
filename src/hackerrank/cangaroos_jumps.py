
def kangaroo(x1, v1, x2, v2):
    xl = min(x1, x2)
    xr = max(x1, x2)
    vl = v1 if xl == x1 else v2
    vr = v2 if xl == x1 else v1

    if xl == xr:
        return True

    if vl <= vr:
        return False

    while xl < xr:
        xl += vl
        xr += vr

    return xl == xr


def kangaroo_kinematic(x1, v1, x2, v2):
    """ Using equation: v1*t + x1 = v2*t + x2 """
    if v1 == v2:
        return x1 == x2

    t = (x2 - x1) / (v1 - v2)
    return 0 <= t == int(t)


if __name__ == '__main__':
    print('YES' if kangaroo(0, 2, 5, 3) else 'NO')
