def solution(str_skilltree, lst_skillset):
    tot_ = 0
    set_ = set(list(str_skilltree))
    for each_skillset in lst_skillset:
        ptr_skilltree = 0
        is_ = True
        for each_skill in each_skillset:
            if each_skill in set_:
                if each_skill == str_skilltree[ptr_skilltree]:
                    ptr_skilltree += 1
                else:
                    is_ = False
                    break
        tot_ += int(is_)

    return tot_


print(solution())
