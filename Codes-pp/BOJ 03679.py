import sys
import math


def rad_(c_a, c_b):
    d_x = c_b[0] - c_a[0]
    d_y = c_b[1] - c_a[1]
    return math.atan2(d_y, d_x)

import sys
from functools import cmp_to_key


def cmp_(c_a, c_b):
    temp_a = c_a[1] * c_b[2]
    temp_b = c_a[2] * c_b[1]
    return 1 if temp_a < temp_b else -1


for _ in range(int(sys.stdin.readline())):
    lst_input = list(map(int, sys.stdin.readline().split()))
    lst_ = []
    for idx_ in range(lst_input[0]):
        lst_.append([idx_, lst_input[2 * idx_ + 1], lst_input[2 * idx_ + 2]])
    lst_.sort(key=lambda x: x[1])
    lst_.sort(key=lambda x: x[2])

    print(lst_)

    for idx_ in range(1, len(lst_)):
        lst_[idx_][1] -= lst_[0][1]
        lst_[idx_][2] -= lst_[0][2]
    lst_[0][1] = 0
    lst_[0][2] = 0
    lst_ = [lst_[0]] + sorted(lst_[1:], key=cmp_to_key(cmp_))
    print(lst_)

    ptr_ = -1
    while lst_[ptr_ - 1][1] * lst_[-1][2] == lst_[ptr_ - 1][2] * lst_[-1][1] and ptr_ > -len(lst_) + 1:
        ptr_ -= 1

    print(lst_)
    lst_[ptr_:].sort(key=lambda x: x[1] * x[1] + x[2] * x[2], reverse=True)

    print(' '.join(map(lambda x: str(x[0]), lst_)))
    print(lst_, ptr_)
exit()
