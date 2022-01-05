import sys
from itertools import permutations as pm

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_p = list(map(int, sys.stdin.readline().split()))

lst_c = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: int(x / y)]

min_ = 10 ** 9
max_ = -10 ** 9

for pm_ in pm([0] * lst_p[0] + [1] * lst_p[1] + [2] * lst_p[2] + [3] * lst_p[3]):
    curr_ = lst_[0]
    for idx_ in range(len(pm_)):
        curr_ = lst_c[pm_[idx_]](curr_, lst_[idx_ + 1])
    min_ = min(min_, curr_)
    max_ = max(max_, curr_)

print(max_)
print(min_)

exit()