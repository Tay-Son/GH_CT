import sys
import copy
from collections import deque

N_ = int(sys.stdin.readline())
grd_input = []
for _ in range(N_):
    grd_input.append(list(map(int, sys.stdin.readline().split())))


def func(grd_, mod_):
    max_ = 0
    for idx_m in range(N_):
        deq_ = deque()
        for idx_s in range(N_):
            if mod_ == 0:
                temp_ = grd_[idx_m][idx_s]
            elif mod_ == 1:
                temp_ = grd_[idx_m][N_ - idx_s - 1]
            elif mod_ == 2:
                temp_ = grd_[idx_s][idx_m]
            else:
                temp_ = grd_[N_ - idx_s - 1][idx_m]

            if temp_:
                deq_.append(temp_)

                if mod_ == 0:
                    grd_[idx_m][idx_s] = 0
                elif mod_ == 1:
                    grd_[idx_m][N_ - idx_s - 1] = 0
                elif mod_ == 2:
                    grd_[idx_s][idx_m] = 0
                else:
                    grd_[N_ - idx_s - 1][idx_m] = 0

        idx_t = 0
        while deq_:
            temp_ = deq_.popleft()
            if deq_ and temp_ == deq_[0]:
                deq_.popleft()
                temp_ *= 2

            if mod_ == 0:
                grd_[idx_m][idx_t] = temp_
            elif mod_ == 1:
                grd_[idx_m][N_ - idx_t - 1] = temp_
            elif mod_ == 2:
                grd_[idx_t][idx_m] = temp_
            else:
                grd_[N_ - idx_t - 1][idx_m] = temp_

            max_ = max(max_, temp_)

            idx_t += 1
    return max_


max_ = 0
for idx_0 in range(4):
    for idx_1 in range(4):
        for idx_2 in range(4):
            for idx_3 in range(4):
                for idx_4 in range(4):
                    grd_ = copy.deepcopy(grd_input)
                    max_ = max(max_, func(grd_, idx_0))
                    max_ = max(max_, func(grd_, idx_1))
                    max_ = max(max_, func(grd_, idx_2))
                    max_ = max(max_, func(grd_, idx_3))
                    max_ = max(max_, func(grd_, idx_4))

print(max_)

exit()
