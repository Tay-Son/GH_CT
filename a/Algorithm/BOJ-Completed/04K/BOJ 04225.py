import sys
import math

INF_ = 1000000009


def rad_(c_a, c_b):
    d_x = c_b[0] - c_a[0]
    d_y = c_b[1] - c_a[1]
    return math.atan2(d_y, d_x)


def diff(c_b, c_a):
    return c_b[0] - c_a[0], c_b[1] - c_a[1]


def ccw(c_a, c_b, c_c):
    d_ba = diff(c_b, c_a)
    d_cb = diff(c_c, c_b)
    return d_ba[0] * d_cb[1] > d_ba[1] * d_cb[0]


N_ = int(sys.stdin.readline())
C_ = 1
while N_:
    lst_ = []
    for idx_ in range(N_):
        lst_.append(tuple(map(int, sys.stdin.readline().split())))

    lst_.sort(key=lambda x_: x_[0])
    lst_.sort(key=lambda x_: x_[1])
    stk_ = [lst_[0]]
    lst_ = sorted(lst_[1:], key=lambda x_: rad_(lst_[0], x_)) + stk_

    ptr_ = 0
    while ptr_ < len(lst_):
        c_c = lst_[ptr_]

        while len(stk_) > 1:
            c_b = stk_.pop()
            c_a = stk_[-1]

            if ccw(c_a, c_b, c_c):
                stk_.append(c_b)
                break

        stk_.append(c_c)
        ptr_ += 1
    min_ = INF_
    for idx_ in range(len(stk_) - 1):
        c_a = stk_[idx_]
        c_b = stk_[idx_ + 1]
        d_ab = diff(c_a, c_b)
        temp_ = (d_ab[0] ** 2 + d_ab[1] ** 2) ** .5
        temp_a = c_a[0] * c_b[1]
        temp_b = c_a[1] * c_b[0]
        max_ = .0

        for idx_sub in range(len(stk_) - 1):
            if idx_sub not in [idx_, idx_ + 1]:
                c_c = stk_[idx_sub]
                max_ = max(max_, abs((temp_a + c_b[0] * c_c[1] + c_c[0] * c_a[1]) -
                                     (temp_b + c_b[1] * c_c[0] + c_c[1] * c_a[0])) / temp_)
        min_ = min(min_, max_)
    str_temp = str(math.ceil(min_ * 100))
    if len(str_temp) < 3:
        str_temp = '0' * (3 - len(str_temp)) + str_temp

    print('Case ' + str(C_) + ': ' + str_temp[:-2] + '.' + str_temp[-2:])
    N_ = int(sys.stdin.readline())
    C_ += 1

exit()
