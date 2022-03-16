def solution(lst_com):
    import heapq as hq

    lst_ = []
    hqu_max = []
    hqu_min = []

    cnt_ = 0
    for each_com in lst_com:
        com_, par_ = each_com.split()
        par_ = int(par_)

        if com_ == 'I':
            lst_.append(True)
            hq.heappush(hqu_max, (-par_, cnt_))
            hq.heappush(hqu_min, (par_, cnt_))
            cnt_ += 1
        else:
            if par_ > 0:
                if hqu_max:
                    _, idx_ = hq.heappop(hqu_max)
                    while not lst_[idx_] and hqu_max:
                        _, idx_ = hq.heappop(hqu_max)
                    lst_[idx_] = False
            else:
                if hqu_min:
                    _, idx_ = hq.heappop(hqu_min)
                    while not lst_[idx_] and hqu_min:
                        _, idx_ = hq.heappop(hqu_min)
                    lst_[idx_] = False

    lst_answer = [0, 0]
    if hqu_max:
        val_, idx_ = hq.heappop(hqu_max)
        while not lst_[idx_] and hqu_max:
            val_, idx_ = hq.heappop(hqu_max)
        if lst_[idx_]:
            lst_answer[0] = -val_

    if hqu_min:
        val_, idx_ = hq.heappop(hqu_min)
        while not lst_[idx_] and hqu_min:
            val_, idx_ = hq.heappop(hqu_min)
        if lst_[idx_]:
            lst_answer[1] = val_

    return lst_answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
