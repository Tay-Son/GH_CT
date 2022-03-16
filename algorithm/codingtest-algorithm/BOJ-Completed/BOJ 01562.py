import sys

DIV_ = 1000000000

N_ = int(sys.stdin.readline())
grd_dp = [[[-1 for _ in range(10)] for _ in range(4)] for _ in range(N_ - 1)]
grd_dp.append([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


def rec_(num_, state_, depth_):
    if grd_dp[depth_][state_][num_] == -1:
        tot_ = 0

        if 0 < num_:
            state_t = state_
            if num_ - 1 == 0:
                state_t |= 1
            tot_ += rec_(num_ - 1, state_t, depth_ + 1)
            tot_ %= DIV_

        if num_ < 9:
            state_t = state_
            if num_ + 1 == 9:
                state_t |= 2
            tot_ += rec_(num_ + 1, state_t, depth_ + 1)
            tot_ %= DIV_

        grd_dp[depth_][state_][num_] = tot_

    print(num_, state_, depth_, grd_dp[depth_][state_][num_])
    return grd_dp[depth_][state_][num_]


tot_ = 0
for num_s in range(1, 9):
    temp_ = rec_(num_s, 0, 0)
    tot_ += temp_
    tot_ %= DIV_
temp_ = rec_(9, 2, 0)
tot_ += temp_
tot_ %= DIV_
# print(temp_)

for each_c in grd_dp:
    for each_ in each_c:
        print(each_)
    print()

print(tot_)
exit()
