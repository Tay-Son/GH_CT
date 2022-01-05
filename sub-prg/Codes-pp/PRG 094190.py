def solution(lst_arrow):
    lst_aux = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    curr_r = 0
    curr_c = 0

    answer_ = 0
    set_ = set()
    set_sub = set()
    set_.add((curr_r, curr_c))
    for arrow_ in lst_arrow:
        ori_r = curr_r
        ori_c = curr_c
        offset_r, offset_c = lst_aux[arrow_]
        curr_r += offset_r
        curr_c += offset_c

        tup_temp = (ori_r, ori_c, curr_r, curr_c)
        tup_temp_r = (curr_r, curr_c, ori_r, ori_c)

        if (curr_r, curr_c) in set_:
            if tup_temp not in set_sub:
                answer_ += 1
                if abs(offset_c) + abs(offset_r) == 2 and \
                        ((ori_r, curr_c, ori_c, curr_r) in set_sub or (ori_c, curr_r, ori_r, curr_c) in set_sub):
                    answer_ += 1
        else:
            set_.add((curr_r, curr_c))
        set_sub.add(tup_temp)
        set_sub.add(tup_temp_r)

    return answer_
