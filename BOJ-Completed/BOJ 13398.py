import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

if N_ == 1:
    print(lst_[0])
else:
    max_ = max(lst_)

    lst_dp = [0]
    temp_ = 0
    for each_ in lst_:
        temp_ = max(0, temp_) + each_
        lst_dp.append(temp_)
        max_ = max(max_, temp_)

    temp_ = 0
    for idx_ in range(N_ - 1, 1, -1):
        temp_ = max(0, temp_) + lst_[idx_]
        max_ = max(max_, temp_ + lst_dp[idx_ - 1])

    print(max_)

exit()
