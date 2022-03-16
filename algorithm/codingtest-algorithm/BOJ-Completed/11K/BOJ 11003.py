import sys
import math

INF_ = 10 ** 9

N_, L_ = map(int, sys.stdin.readline().split())

max_depth = math.ceil(math.log2(N_))
cch_ = 2 ** max_depth
tre_ = [0 for _ in range(cch_)] + \
       list(map(int, sys.stdin.readline().split())) + \
       [INF_ for _ in range(cch_ - N_)]

for idx_tre in range(cch_ - 1, 0, -1):
    tre_[idx_tre] = min(tre_[2 * idx_tre], tre_[2 * idx_tre + 1])

lst_ans = []
for idx_e in range(N_):
    idx_s = max(0, idx_e - L_ + 1) + cch_
    idx_e += cch_

    min_ = INF_
    while idx_s < idx_e:
        if idx_s ^ 1:
            min_ = min(min_, tre_[idx_s])
            idx_s += 1
        if idx_e ^ 0:
            min_ = min(min_, tre_[idx_e])
            idx_e -= 1
        idx_s //= 2
        idx_e //= 2

    if idx_s == idx_e:
        min_ = min(min_, tre_[idx_s])

    lst_ans.append(min_)

print(' '.join(map(str, lst_ans)))

exit()