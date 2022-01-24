import sys
from collections import deque

N_ = int(sys.stdin.readline())
grd_ = [[[] for _ in range(2 * N_ - 1)] for _ in range(2)]
for idx_r in range(N_):
    for idx_c, value_ in enumerate(map(int, sys.stdin.readline().split())):
        idx_ = 2 * (N_ - 1 - abs((idx_r + idx_c) - (N_ - 1))) + (0 if (idx_r + idx_c) - (N_ - 1) <= 0 else 1)
        if value_:
            temp_ = idx_r - idx_c + N_ - 1
            grd_[idx_].append(temp_)
            bit_ = 1 << temp_
            state_ |= bit_

print(grd_)

min_ = 0
que_ = deque([(0, 0, state_)])
while que_:




while hqu_:
    cnt_, depth_, state_ = hq.heappop(hqu_)
    if state_:
        if depth_ == 2 * N_ - 1:
            min_ = min(min_, cnt_)
        else:
            for num_ in grd_[depth_]:
                bit_ = 1 << num_
                if state_ & bit_:
                    state_temp = state_ ^ bit_
                    hq.heappush(hqu_, (cnt_ - 1, depth_ + 1, state_temp))
            hq.heappush(hqu_, (cnt_, depth_ + 1, state_))

print(-min_)

exit()
