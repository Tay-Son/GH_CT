import sys
from itertools import combinations as cb

N_ = int(sys.stdin.readline())

lst_ = []
for _ in range(N_):
    lst_.append(tuple(map(int, sys.stdin.readline().split())))

grd_ = [[0 for _ in range(N_)] for _ in range(N_)]
for idx_a, idx_b in cb(range(N_), 2):
    x1, y1 = lst_[idx_a]
    x2, y2 = lst_[idx_b]

    temp_ = (x1 - x2) ** 2 + (y1 - y2) ** 2
    grd_[idx_a][idx_b] = temp_
    grd_[idx_b][idx_a] = temp_

min_ = 1000000009
min_idx = 0

for idx_, lst_temp in enumerate(grd_):
    print(lst_temp, max(lst_temp))
    temp_ = max(lst_temp)
    if temp_ < min_:
        min_ = temp_
        min_idx = idx_

print(lst_[min_idx][0], lst_[min_idx][1])

exit()
