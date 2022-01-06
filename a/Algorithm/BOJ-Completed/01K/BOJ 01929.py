import sys
import math

M_, N_ = map(int, sys.stdin.readline().split())

lst_is = [True for _ in range(N_ + 1)]

lst_is[0] = False
if N_ > 0:
    lst_is[1] = False
if N_ > 1:
    for num_ in range(2, math.ceil(N_ ** 0.5) + 1):
        if lst_is[num_]:
            for idx_ in range(num_ * num_, N_ + 1, num_):
                lst_is[idx_] = False

for idx_ in range(M_, N_ + 1):
    if lst_is[idx_]:
        print(idx_)

exit()