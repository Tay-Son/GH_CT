def func_(lst_is_visited, grp_, idx_s):
    lst_is_visited[idx_s] = True
    tot_ = 0
    for idx_e in grp_[idx_s]:
        if not lst_is_visited[idx_e]:
            tot_ += 1 + func_(lst_is_visited, grp_, idx_e)
    return tot_


def solution(N_, lst_):
    grp_win = [[] for _ in range(N_ + 1)]
    grp_loss = [[] for _ in range(N_ + 1)]
    for winner_, loser_ in lst_:
        grp_win[winner_].append(loser_)
        grp_loss[loser_].append(winner_)

    answer_ = 0
    for idx_s in range(1, N_ + 1):
        lst_is_visited = [False for _ in range(N_ + 1)]
        if func_(lst_is_visited, grp_win, idx_s) + func_(lst_is_visited, grp_loss, idx_s) == N_ - 1:
            answer_ += 1

    return answer_


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
