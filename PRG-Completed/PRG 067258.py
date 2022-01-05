def solution(lst_gem):
    lst_ = []
    dct_gem = {}

    cnt_ = 0
    for gem_ in lst_gem:
        if gem_ not in dct_gem:
            dct_gem[gem_] = cnt_
            cnt_ += 1
        lst_.append(dct_gem[gem_])

    lst_answer = [1, len(lst_gem)]
    dct_cnt = {idx_: 0 for idx_ in dct_gem.values()}
    tot_ = 0
    ptr_s = 0
    for ptr_e in range(len(lst_)):
        idx_target = lst_[ptr_e]
        if not dct_cnt[idx_target]:
            tot_ += 1
        dct_cnt[idx_target] += 1

        while tot_ == cnt_:
            if (ptr_e - ptr_s) < (lst_answer[1] - lst_answer[0]):
                lst_answer = [ptr_s + 1, ptr_e + 1]

            idx_target = lst_[ptr_s]
            if dct_cnt[idx_target] == 1:
                tot_ -= 1
            dct_cnt[idx_target] -= 1
            ptr_s += 1

    return lst_answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
