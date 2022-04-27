import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

lst_a = []
lst_d = []

for idx_, (a_, b_) in enumerate(zip(lst_[:-1], lst_[1:])):
    if a_ > b_:
        lst_a.append(idx_)
    elif a_ < b_:
        lst_d.append(idx_)

if not len(lst_a) or not len(lst_d):
    print(0)
else:
    min_ = N_
    if len(lst_a) == 1 and lst_[0] >= lst_[-1]:
        min_ = min(min_, lst_a[0] + 1)
    if len(lst_d) == 1 and lst_[0] <= lst_[-1]:
        min_ = min(min_, lst_d[0] + 1)
    if min_ == N_:
        print(-1)
    else:
        print(min_)

exit()
