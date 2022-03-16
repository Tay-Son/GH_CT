import sys

INF_ = int(1e9)

N_ = int(sys.stdin.readline())
grd_ = [list(map(int, sys.stdin.readline().split())) for _ in range(N_)]
grd_dp = [[-1 for _ in range(2 ** N_)] for _ in range(N_)]


def func(curr_, visited_):
    if grd_dp[curr_][visited_] == -1:
        if visited_ == (1 << N_) - 1:
            temp_ = grd_[curr_][0]
            if temp_ > 0:
                grd_dp[curr_][visited_] = temp_
            else:
                grd_dp[curr_][visited_] = INF_
        else:
            min_ = INF_
            for next_ in range(N_):
                bt_next = 1 << next_
                if next_ != curr_ and not visited_ & bt_next:
                    temp_ = grd_[curr_][next_]
                    if temp_:
                        min_ = min(min_, func(next_, visited_ | bt_next) + temp_)
            grd_dp[curr_][visited_] = min_
    return grd_dp[curr_][visited_]


print(func(0, 1))

exit()