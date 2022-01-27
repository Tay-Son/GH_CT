import sys

N_ = int(sys.stdin.readline())

# grd_ = [[1.0 for _ in range(N_)]] + [list(map(lambda x: int(x) / 100, sys.stdin.readline().split())) for _ in range(N_)]
grd_ = [list(map(lambda x: int(x) / 100, sys.stdin.readline().split())) for _ in range(N_)]
lst_dp = [-1 for _ in range(2 ** N_)]
for o_sh in range(N_):
    bit_ = 1 << o_sh
    lst_dp[bit_] = grd_[0][o_sh]

for each_ in grd_:
    print(each_)


def rec_(bit_, depth_):
    print(bin(bit_)[2:])
    if lst_dp[bit_] == -1:
        max_ = 0
        depth_ -= 1
        for o_sh in range(N_):
            bit_c = 1 << o_sh
            if bit_ & bit_c:
                max_ = max(max_, grd_[depth_][o_sh] * rec_(bit_ ^ bit_c, depth_))
        lst_dp[bit_] = max_

    return lst_dp[bit_]


print(rec_(2 ** N_ - 1, N_) * 100)
print(lst_dp)

exit()
