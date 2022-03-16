import sys
from collections import deque

N_ = int(sys.stdin.readline())

grd_ = [[[] for _ in range(N_ - o_)] for o_ in range(2)]
bit_ = [0, 0]
for idx_r in range(N_):
    for idx_c, value_ in enumerate(map(int, sys.stdin.readline().split())):
        temp_ = idx_r + idx_c
        idx_, o_ = divmod(temp_, 2)
        if value_:
            temp_ = idx_r - idx_c + N_ - 1
            grd_[o_][idx_].append(temp_)
            bit_[o_] |= 1 << temp_

for each_ in grd_:
    print(each_)

tot_ = 0
for o_ in range(2):
    que_ = deque([(0, 0, bit_[o_])])
    max_ = 0
    while que_:
        cnt_, depth_, bit_c = que_.popleft()
        if bit_:
            if depth_ == N_ - o_:
                max_ = max(max_, cnt_)
            else:
                for num_ in grd_[o_][depth_]:
                    bit_temp = 1 << num_
                    if bit_c & bit_temp:
                        que_.append((cnt_ + 1, depth_ + 1, bit_c ^ bit_temp))
                que_.append((cnt_, depth_ + 1, bit_c))
        else:
            max_ = max(max_, cnt_)
    tot_ += max_
print(tot_)

exit()
