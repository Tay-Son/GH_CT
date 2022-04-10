def solution(ptr_s, ptr_e):
    thr_ = 10000000
    lst_ans = []
    for idx_ in range(ptr_s, ptr_e + 1):
        if idx_ < 2:
            lst_ans.append(0)
        else:
            for idx_sub in range(2, int(idx_ ** .5) + 1):
                div_, mod_ = divmod(idx_, idx_sub)
                if not mod_ and div_ <= thr_:
                    lst_ans.append(div_)
                    break
            else:
                lst_ans.append(1)
    return lst_ans
