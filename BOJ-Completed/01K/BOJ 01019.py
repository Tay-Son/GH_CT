import sys

N_ = int(sys.stdin.readline())
lst_ = [0 for i in range(10)]
cache_ = 1
while N_ != 0:
    while N_ % 10 != 9:
        for target_ in map(int, list(str(N_))):
            lst_[target_] += cache_
        N_ -= 1
    if N_ < 10:
        for cnt_ in range(N_ + 1):
            lst_[cnt_] += cache_
        lst_[0] -= cache_
        break
    else:
        for cnt_ in range(10):
            lst_[cnt_] += (N_ // 10 + 1) * cache_
    lst_[0] -= cache_
    cache_ *= 10
    N_ //= 10
print(' '.join(map(str, lst_)))
