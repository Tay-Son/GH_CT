import sys

N_ = int(sys.stdin.readline())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

lst_aux = [(0, 1), (1, 0), (1, 1)]
grd_dp = [[[-1 for _ in range(3)] for _ in range(N_)] for _ in range(N_)]
grd_dp[N_ - 1][N_ - 2][0] = 1
grd_dp[N_ - 2][N_ - 1][1] = 1
grd_dp[N_ - 2][N_ - 2][2] = 1


def func_(i_r, i_c, state_):
    if grd_dp[i_r][i_c][state_] == -1:
        global N_
        grd_dp[i_r][i_c][state_] += 1

        o_r, o_c = lst_aux[state_]
        a_r = i_r + o_r
        a_c = i_c + o_c
        cnt_ = 0

        t_r, t_c = a_r, a_c + 1
        if 0 <= t_r < N_ and 0 <= t_c < N_ and not grd_[t_r][t_c]:
            cnt_ += 1
            if state_ != 1:
                grd_dp[i_r][i_c][state_] += func_(a_r, a_c, 0)

        t_r, t_c = a_r + 1, a_c
        if 0 <= t_r < N_ and 0 <= t_c < N_ and not grd_[t_r][t_c]:
            cnt_ += 1
            if state_ != 0:
                grd_dp[i_r][i_c][state_] += func_(a_r, a_c, 1)

        if cnt_ >= 2:
            t_r, t_c = a_r + 1, a_c + 1
            if 0 <= t_r < N_ and 0 <= t_c < N_ and not grd_[t_r][t_c]:
                grd_dp[i_r][i_c][state_] += func_(a_r, a_c, 2)

    return grd_dp[i_r][i_c][state_]


print(func_(0, 0, 0))

exit()
