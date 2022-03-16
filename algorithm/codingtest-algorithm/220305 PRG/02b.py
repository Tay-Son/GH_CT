def solution(h_, w_, n_, grd_):
    tot_ = 0
    for idx_h in range(h_):
        lst_ = []
        curr_ = 0
        for idx_w in range(w_):
            val_ = grd_[idx_h][idx_w]
            if val_ == '1':
                curr_ += 1
            else:
                if curr_:
                    lst_.append(curr_)
                curr_ = 0
        if curr_:
            lst_.append(curr_)

        for each_ in lst_:
            if each_ == n_:
                tot_ += 1

    for idx_w in range(w_):
        lst_ = []
        curr_ = 0
        for idx_h in range(h_):
            val_ = grd_[idx_h][idx_w]
            if val_ == '1':
                curr_ += 1
            else:
                if curr_:
                    lst_.append(curr_)
                curr_ = 0
        if curr_:
            lst_.append(curr_)

        for each_ in lst_:
            if each_ == n_:
                tot_ += 1

    for s_w in range(-h_, w_):
        lst_ = []
        curr_ = 0
        for o_ in range(h_):
            idx_w, idx_h = s_w + o_, o_

            if 0 <= idx_w < w_:
                val_ = grd_[idx_h][idx_w]
                if val_ == '1':
                    curr_ += 1
                else:
                    if curr_:
                        lst_.append(curr_)
                    curr_ = 0
        if curr_:
            lst_.append(curr_)

        for each_ in lst_:
            if each_ == n_:
                tot_ += 1
        print(lst_)

    for s_w in range(w_ + h_):
        lst_ = []
        curr_ = 0
        for o_ in range(h_):
            idx_w, idx_h = s_w - o_, o_

            if 0 <= idx_w < w_:
                val_ = grd_[idx_h][idx_w]
                if val_ == '1':
                    curr_ += 1
                else:
                    if curr_:
                        lst_.append(curr_)
                    curr_ = 0
        if curr_:
            lst_.append(curr_)

        for each_ in lst_:
            if each_ == n_:
                tot_ += 1

    return tot_


for h_, w_, n_, grd_ in [
    (7, 9, 4, ["111100000", "000010011", "111100011", "111110011", "111100011", "111100010", "111100000"]),
    (5, 5, 5, ["11111", "11111", "11111", "11111", "11111"])
]:
    print(solution(h_, w_, n_, grd_))
