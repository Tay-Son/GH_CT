import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(float, sys.stdin.readline().split()))
lst_sub = [lst_[idx_] * (1 - lst_[idx_ + 1]) + (1 - lst_[idx_]) * lst_[idx_ + 1] for idx_ in range(N_ - 1)]

print(sum(lst_) + sum(lst_sub))

exit()
