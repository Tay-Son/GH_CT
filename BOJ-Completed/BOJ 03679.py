import sys
from functools import cmp_to_key


def ccw_(coord_a, coord_b, coord_c):
    temp_ = (coord_b[0] - coord_a[0]) * (coord_c[1] - coord_b[1]) - \
            (coord_c[0] - coord_b[0]) * (coord_b[1] - coord_a[1])
    return 1 if temp_ > 0 else -1 if temp_ else 0


def dist_(coord_a):
    return coord_a[0] ** 2 + coord_a[1] ** 2


def compare_(a_, b_):
    coord_a = a_[0]
    coord_b = b_[0]

    if ccw_([0, 0], coord_a, coord_b) > 0:
        return -1
    elif ccw_([0, 0], coord_a, coord_b) < 0:
        return 1
    else:
        if dist_(coord_a) < dist_(coord_b):
            return -1
        else:
            return 1


for _ in range(int(sys.stdin.readline())):
    lst_input = list(map(int, sys.stdin.readline().split()))
    N_ = lst_input[0]
    lst_ = []
    for idx_ in range(N_):
        lst_.append([[lst_input[2 * idx_ + 1], lst_input[2 * idx_ + 2]], idx_])

    lst_.sort(key=lambda x: x[0][1])
    lst_.sort(key=lambda x: x[0][0])
    lst_ = [[[each_[0][0] - lst_[0][0][0], each_[0][1] - lst_[0][0][1]], each_[1]] for each_ in lst_]
    lst_[1:] = sorted(lst_[1:], key=cmp_to_key(compare_))

    cnt_ = N_ - 1
    while ccw_([0, 0], lst_[cnt_ - 1][0], lst_[cnt_][0]) == 0:
        cnt_ -= 1
    lst_[cnt_:] = reversed(lst_[cnt_:])

    print(' '.join(map(lambda x: str(x[1]), lst_)))
exit()
