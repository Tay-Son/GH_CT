import sys
from collections import defaultdict

N_, H_ = map(int, sys.stdin.readline().split())

dct_ = defaultdict(int)
for _ in range(0, N_, 2):
    dct_[int(sys.stdin.readline())] -= 1
    dct_[H_ - int(sys.stdin.readline())] += 1

lst_ = sorted(dct_.items()) + [(H_, N_ // 2)]

curr_ = N_ // 2
min_ = curr_
tot_ = lst_[0][0]
for idx_ in range(len(lst_) - 1):
    curr_ += lst_[idx_][1]
    if curr_ == min_:
        tot_ += lst_[idx_ + 1][0] - lst_[idx_][0]
    elif curr_ < min_:
        min_ = curr_
        tot_ = lst_[idx_ + 1][0] - lst_[idx_][0]
print(str(min_) + ' ' + str(tot_))

exit()
