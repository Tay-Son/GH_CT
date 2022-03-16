def solution(lst_weights, grd_):
    N_ = len(lst_weights)
    dct_weight = {}
    dct_winrate = {}
    dct_hww = {}

    for idx_s in range(N_):
        tot_game = 0
        tot_win = 0
        tot_hww = 0
        for idx_t in range(N_):
            if idx_s != idx_t:
                if grd_[idx_s][idx_t] != 'N':
                    tot_game += 1
                    if grd_[idx_s][idx_t] == 'W':
                        tot_win += 1
                        if lst_weights[idx_s] < lst_weights[idx_t]:
                            tot_hww += 1

        dct_weight[idx_s] = lst_weights[idx_s]
        dct_hww[idx_s] = tot_hww
        if tot_game:
            tot_win /= tot_game
        dct_winrate[idx_s] = tot_win

    lst_answer = list(range(1, N_ + 1))
    lst_answer.sort(key=lambda idx_: -dct_weight[idx_ - 1])
    lst_answer.sort(key=lambda idx_: -dct_hww[idx_ - 1])
    lst_answer.sort(key=lambda idx_: -dct_winrate[idx_ - 1])

    return lst_answer


print(solution(
    [50, 82, 75, 120],
    ["NLWL", "WNLL", "LWNW", "WWLN"]))
