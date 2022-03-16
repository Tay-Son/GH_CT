def solution(grd_):
    R_, C_ = len(grd_), len(grd_[0])

    lst_state = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    grd_iv = [[[False for _ in range(4)] for _ in range(C_)] for _ in range(R_)]

    lst_answer = []
    for idx_r in range(R_):
        for idx_c in range(C_):
            for state_ in range(4):
                if not grd_iv[idx_r][idx_c][state_]:
                    grd_iv[idx_r][idx_c][state_] = True

                    curr_r = (idx_r + lst_state[state_][0]) % R_
                    curr_c = (idx_c + lst_state[state_][1]) % C_

                    if grd_[curr_r][curr_c] == 'L':
                        curr_s = (state_ - 1) % 4
                    elif grd_[curr_r][curr_c] == 'R':
                        curr_s = (state_ + 1) % 4
                    else:
                        curr_s = state_
                    tot_ = 1

                    while curr_r != idx_r or curr_c != idx_c or curr_s != state_:
                        grd_iv[curr_r][curr_c][curr_s] = True
                        curr_r = (curr_r + lst_state[curr_s][0]) % R_
                        curr_c = (curr_c + lst_state[curr_s][1]) % C_

                        if grd_[curr_r][curr_c] == 'L':
                            curr_s = (curr_s - 1) % 4
                        elif grd_[curr_r][curr_c] == 'R':
                            curr_s = (curr_s + 1) % 4
                        tot_ += 1

                    lst_answer.append(tot_)
    lst_answer.sort()
    return lst_answer