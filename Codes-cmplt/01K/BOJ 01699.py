import sys

INF_ = 10 ** 9
N_ = int(sys.stdin.readline())

lst_dp = [-1 for _ in range(N_ + 1)]
lst_dp[0] = 0


def func(num_):
    min_ = INF_
    for idx_ in range(int(num_ ** .5), 0, -1):
        div_, mod_ = divmod(num_, idx_ ** 2)
        if div_ >= min_:
            break
        if lst_dp[mod_] == -1:
            lst_dp[mod_] = func(mod_)
        min_ = min(min_, lst_dp[mod_] + div_)

    return min_


print(func(N_))

exit()