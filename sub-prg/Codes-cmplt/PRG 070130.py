def solution(lst_):
    N_ = len(lst_)
    if N_ == 1:
        return 0
    elif N_ == 2:
        return 2
    else:
        lst_sub = [0 for _ in range(N_)]
        lst_is = [0 for _ in range(N_)]

        lst_is[0] = 1
        lst_is[1] = -1
        lst_sub[lst_[0]] += 1
        if lst_[0] != lst_[1]:
            lst_sub[lst_[1]] += 1

        for idx_ in range(2, N_ - 1):
            if not lst_is[idx_]:
                if lst_[idx_ - 1] != lst_[idx_]:
                    if lst_[idx_ - 2] == lst_[idx_]:
                        if not lst_is[idx_ - 2] == 1:
                            lst_is[idx_] = -1
                            lst_sub[lst_[idx_]] += 1
                        else:
                            if lst_[idx_] != lst_[idx_ + 1]:
                                lst_is[idx_] = 1
                                lst_sub[lst_[idx_]] += 1
                            else:
                                lst_is[idx_] = 1
                                lst_is[idx_ + 1] = -1
                                lst_sub[lst_[idx_]] += 1
                    else:
                        lst_is[idx_] = -1
                        lst_sub[lst_[idx_]] += 1
                else:
                    if not lst_is[idx_ - 1]:
                        lst_is[idx_] = -1
                        lst_sub[lst_[idx_]] += 1
                    else:
                        if lst_[idx_] != lst_[idx_ + 1]:
                            lst_is[idx_] = 1
                            lst_sub[lst_[idx_]] += 1
                        else:
                            lst_is[idx_] = 1
                            lst_is[idx_ + 1] = -1
                            lst_sub[lst_[idx_]] += 1

        if not lst_is[-1]:
            if lst_[-2] != lst_[-1]:
                if lst_[-3] == lst_[-1] and lst_is[-3] == 1:
                    pass
                else:
                    lst_is[-1] = -1
                    lst_sub[lst_[-1]] += 1

        print(lst_)
        print(lst_is)
        print(lst_sub)
        return max(lst_sub) * 2


print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
print()
print(solution([0 for _ in range(11)]))
print()
print(solution([0,0,0,0,0,0,0,0,0,1,1]))
