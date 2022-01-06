import sys

M_ = int(sys.stdin.readline())
N_ = int(sys.stdin.readline())

tot_ = 0
min_ = 10001
lst_ = [True for _ in range(N_ + 1)]
lst_[0], lst_[1] = False, False
for num_ in range(2, N_ + 1):
    if lst_[num_]:
        if num_ >= M_:
            tot_ += num_
            min_ = min(min_, num_)
        for num_sub in range(num_ + num_, N_ + 1, num_):
            lst_[num_sub] = False

if tot_:
    print(tot_)
    print(min_)
else:
    print(-1)
exit()
