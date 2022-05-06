def solution(grd_, lst_skill):
    N_, M_ = len(grd_), len(grd_[0])
    grd_dp = [[0 for _ in range(M_ + 1)] for _ in range(N_ + 1)]

    for skill_ in lst_skill:
        type_, n1_, m1_, n2_, m2_, degree_ = skill_
        degree_ = -degree_ if type_ == 2 else degree_
        grd_dp[n1_][m1_] -= degree_
        grd_dp[n1_][m2_ + 1] += degree_
        grd_dp[n2_ + 1][m1_] += degree_
        grd_dp[n2_ + 1][m2_ + 1] -= degree_

    for each_ in grd_dp:
        print(each_)
    print()

    for idx_n in range(N_):
        curr_ = 0
        for idx_m in range(M_):
            curr_ += grd_dp[idx_n][idx_m]
            grd_dp[idx_n][idx_m] = curr_

    for idx_m in range(M_):
        curr_ = 0
        for idx_n in range(N_):
            curr_ += grd_dp[idx_n][idx_m]
            grd_dp[idx_n][idx_m] = curr_

    for each_ in grd_dp:
        print(each_)
    print()

    tot_ = 0
    for idx_n in range(N_):
        for idx_m in range(M_):
            if grd_dp[idx_n][idx_m] + grd_[idx_n][idx_m] > 0:
                tot_ += 1
    return tot_


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
