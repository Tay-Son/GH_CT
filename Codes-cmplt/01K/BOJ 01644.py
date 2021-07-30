import sys
import math

N_ = int(sys.stdin.readline())

lst_is = [True for _ in range(N_ + 1)]
lst_is[0] = False
if N_ > 0:
    lst_is[1] = False

if N_ > 1:
    for num_ in range(2, math.ceil(N_ ** 0.5) + 1):
        if lst_is[num_]:
            for idx_ in range(num_ * 2, N_ + 1, num_):
                lst_is[idx_] = False

lst_ = [0]
sum_ = 0
for idx_ in range(1, N_ + 1):
    if lst_is[idx_]:
        sum_ += idx_
        lst_.append(sum_)

idx_s = 0
cnt_ = 0
for idx_e in range(1, len(lst_)):
    temp_ = lst_[idx_e] - lst_[idx_s]
    while temp_ >= N_:
        if temp_ == N_:
            cnt_ += 1
        idx_s += 1
        temp_ = lst_[idx_e] - lst_[idx_s]
print(cnt_)

exit()