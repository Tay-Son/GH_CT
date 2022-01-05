def solution(N_, T_, M_, P_):
    P_ -= 1

    dct_not = {idx_: val_ for idx_, val_ in zip(range(16), list('0123456789ABCDEF'))}

    def not_(N_, cnt_abs):
        str_answer = ''
        while cnt_abs >= N_:
            cnt_abs, rem_ = divmod(cnt_abs, N_)
            str_answer = dct_not[rem_] + str_answer
        str_answer = dct_not[cnt_abs] + str_answer
        return str_answer

    cnt_ = 0
    str_target = ''
    cnt_abs = 0
    str_answer = ''
    while len(str_answer) < T_:
        if cnt_ + 1 < len(str_target):
            pass
        else:
            str_target += not_(N_, cnt_abs)
            cnt_abs += 1

        if cnt_ % M_ == P_:
            str_answer += str_target[cnt_]

        cnt_ += 1

    print(str_target)

    return str_answer


print(solution(16, 16, 2, 1))
