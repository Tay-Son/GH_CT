import sys
import math


def rad_(c_a, c_b):
    d_x = c_b[0] - c_a[0]
    d_y = c_b[1] - c_a[1]
    return math.atan2(d_y, d_x)


for _ in range(int(sys.stdin.readline())):
    lst_input = list(map(int, sys.stdin.readline().split()))
    lst_ = []
    for idx_ in range(lst_input[0]):
        lst_.append((lst_input[2 * idx_], lst_input[2 * idx_ + 1]))
    lst_c = list(range(len(lst_)))
    lst_c.sort(key=lambda x: lst_[x][0])
    lst_c.sort(key=lambda x: lst_[x][1])
    lst_c = [lst_c[0]] + sorted(lst_c[1:], key=lambda x: rad_(lst_[lst_c[0]], lst_[x]))

    ptr_ = -1
    r_ = rad_(lst_[lst_c[0]], lst_[lst_c[ptr_]])
    while rad_(lst_[lst_c[0]], lst_[lst_c[ptr_ - 1]]) == r_:
        ptr_ -= 1
    lst_c = lst_c[:ptr_] + sorted(lst_c[ptr_:], key=lambda x: lst_[x][1], reverse=True)

    print(' '.join(map(str, lst_c)))

exit()
