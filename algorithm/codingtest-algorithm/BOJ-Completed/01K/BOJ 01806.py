import sys

N_, S_ = map(int, sys.stdin.readline().split())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_sum = [0]
sum_ = 0
for each_ in lst_:
    sum_ += each_
    lst_sum.append(sum_)

min_ = N_+1
idx_s = 0
for idx_e in range(1, N_ + 1):
    while lst_sum[idx_e] - lst_sum[idx_s] >= S_:
        min_ = min(min_, idx_e - idx_s)
        idx_s += 1
if min_ == N_+1:
    min_ = 0
print(min_)

exit()