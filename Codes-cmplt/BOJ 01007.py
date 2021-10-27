import sys
from itertools import combinations as cb

for _ in range(int(sys.stdin.readline())):
    lst_ = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

    min_ = 300000000000.0
    x_p = 0
    y_p = 0
    for c_x, c_y in lst_:
        x_p += c_x
        y_p += c_y
    x_p /= 2
    y_p /= 2

    for lst_cb in cb(range(len(lst_)), len(lst_) // 2):
            x_t, y_t = x_p, y_p
        for idx_ in lst_cb:
            c_x, c_y = lst_[idx_]
            x_t -= c_x
            y_t -= c_y

        min_ = min(min_, x_t ** 2 + y_t ** 2)
    print(min_ ** .5 * 2)

exit()
