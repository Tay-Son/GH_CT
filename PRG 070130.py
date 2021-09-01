def solution(lst_):
    lst_sub = [0 for _ in range(len(lst_))]

    if len(lst_) == 1:
        pass
    elif len(lst_) == 2:
        lst_sub[lst_[0]] += 1
    else:
        lst_sub[lst_[1]] += 1
        if lst_[0] != lst_[1] and lst_[0] != lst_[2]:
            lst_sub[lst_sub[0]] += 1

        for idx_ in range(2, len(lst_)):
            if lst_[idx_ - 1] != lst_[idx_]:
                lst_sub[lst_[idx_]] += 1
                if lst_[idx_ - 2] == lst_[idx_ - 1]:
                    lst_[idx_ - 1] += 1
            elif lst_[idx_] == lst_[idx_ - 2]:
                lst_sub[lst_[idx_]] += 1


    print(lst_sub)
    return max(lst_sub) * 2


print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
