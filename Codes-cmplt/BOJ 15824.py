import sys

DIV_ = 1000000007

dct_dp = {}


def my_pow_2(val_):
    if val_ not in dct_dp:
        if not val_:
            dct_dp[val_] = 1
        elif val_ % 2:
            dct_dp[val_] = my_pow_2(val_ - 1) * 2 % DIV_
        else:
            temp_ = my_pow_2(val_ // 2)
            dct_dp[val_] = temp_ * temp_ % DIV_
    return dct_dp[val_]


N_ = int(sys.stdin.readline())
lst_ = sorted(list(map(int, sys.stdin.readline().split())))
tot_ = 0
for idx_ in range(N_):
    tot_ += lst_[idx_] * (my_pow_2(idx_) - my_pow_2(N_ - idx_ - 1))
    tot_ %= DIV_

print(tot_)

exit()
