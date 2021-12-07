import sys


def intersect_(v0, v1, v2, v3):
    p_x = (v0[0] * v1[1] - v0[1] * v1[0]) * (v2[0] - v3[0]) - (v2[0] * v3[1] - v2[1] * v3[0]) * (v0[0] - v1[0])
    p_y = (v0[0] * v1[1] - v0[1] * v1[0]) * (v2[1] - v3[1]) - (v2[0] * v3[1] - v2[1] * v3[0]) * (v0[1] - v1[1])
    p_ = (v0[0] - v1[0]) * (v2[1] - v3[1]) - (v0[1] - v1[1]) * (v2[0] - v3[0])

    if not p_:
        if v1 == v2 and v0 <= v2:
            print(v1[0], v1[1])
        elif v0 == v3 and v2 <= v0:
            print(v0[0], v0[1])
    else:
        print(p_x / p_, p_y / p_)


def ccw_(v0, v1, v2):
    temp_ = (v0[0] * v1[1] + v1[0] * v2[1] + v2[0] * v0[1]) - (v1[0] * v0[1] + v2[0] * v1[1] + v0[0] * v2[1])
    if temp_ > 0:
        return 1
    elif temp_ == 0:
        return 0
    else:
        return -1


lst_v = []
for _ in range(2):
    x0, y0, x1, y1 = map(int, sys.stdin.readline().split())
    lst_v.append((x0, y0))
    lst_v.append((x1, y1))

ccw0 = ccw_(lst_v[0], lst_v[1], lst_v[2]) * ccw_(lst_v[0], lst_v[1], lst_v[3])
ccw1 = ccw_(lst_v[2], lst_v[3], lst_v[0]) * ccw_(lst_v[2], lst_v[3], lst_v[1])

if not ccw0 and not ccw1:
    print('if')
    if lst_v[0] > lst_v[1]:
        lst_v[1], lst_v[0] = lst_v[0], lst_v[1]
    if lst_v[2] > lst_v[3]:
        lst_v[3], lst_v[2] = lst_v[2], lst_v[3]

    if lst_v[0] <= lst_v[3] and lst_v[2] <= lst_v[1]:
        print(1)
        intersect_(lst_v[0], lst_v[1], lst_v[2], lst_v[3])
    else:
        print(0)
else:
    print('else')
    if ccw0 <= 0 and ccw1 <= 0:
        print(1)
        intersect_(lst_v[0], lst_v[1], lst_v[2], lst_v[3])
    else:
        print(0)

exit()
