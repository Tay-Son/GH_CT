import sys
from functools import cmp_to_key
from itertools import combinations as cb


def diff(c_b, c_a):
    return c_b[0] - c_a[0], c_b[1] - c_a[1]


def cmp_(c_a, c_b):
    temp_a = c_a[0] * c_b[1]
    temp_b = c_a[1] * c_b[0]
    if temp_a != temp_b:
        return 1 if temp_a < temp_b else -1
    elif c_a[1] != c_b[1]:
        return 1 if c_a[1] < c_b[1] else -1
    else:
        return 1 if c_a[0] < c_b[0] else -1


def ccw(c_a, c_b, c_c):
    d_ba = diff(c_b, c_a)
    d_cb = diff(c_c, c_b)
    return d_ba[0] * d_cb[1] > d_ba[1] * d_cb[0]


N_ = int(sys.stdin.readline())
lst_c = []

for idx_ in range(N_):
    c_x, c_y = map(int, sys.stdin.readline().split())
    lst_c.append((c_x, c_y))
lst_c.sort(key=lambda x: x[1])

lst_d = [(0, 0)]
for idx_ in range(1, N_):
    lst_d.append(diff(lst_c[idx_], lst_c[0]))
lst_d = [lst_d[0]] + sorted(lst_d[1:], key=cmp_to_key(cmp_))

stk_ = []
ptr_ = 0
while ptr_ < len(lst_d):
    c_c = lst_d[ptr_]
    while len(stk_) > 2:
        c_b = stk_.pop()
        c_a = stk_[-1]
        if ccw(c_a, c_b, c_c):
            stk_.append(c_b)
            break
    stk_.append(c_c)
    ptr_ += 1

c_c = stk_[0]
while len(stk_) > 3:
    c_b = stk_.pop()
    c_a = stk_[-1]
    if ccw(c_a, c_b, c_c):
        stk_.append(c_b)
        break

print(stk_)
max_ = 0
for c_a, c_b in cb(stk_, 2):
    d_x, d_y = diff(c_a, c_b)
    max_ = max(max_, d_x ** 2 + d_y ** 2)

print(max_ ** .5)

exit()
