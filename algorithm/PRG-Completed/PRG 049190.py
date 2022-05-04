def solution(lst_arrow):
    lst_aux = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    set_pos = set()
    set_line = set()

    curr_r = 0
    curr_c = 0
    set_pos.add((curr_r, curr_c))

    answer_ = 0
    for arrow_ in lst_arrow:
        ori_r = curr_r
        ori_c = curr_c
        offset_r, offset_c = lst_aux[arrow_]
        curr_r += offset_r
        curr_c += offset_c

        line_ = (min(ori_r, curr_r), min(ori_c, curr_c), arrow_ % 4)
        if line_ not in set_line:
            if (curr_r, curr_c) in set_pos:
                answer_ += 1
            if arrow_ % 2 and (min(ori_r, curr_r), min(ori_c, curr_c), (arrow_ + 2) % 4) in set_line:
                answer_ += 1

        set_line.add(line_)
        set_pos.add((curr_r, curr_c))
    return answer_
