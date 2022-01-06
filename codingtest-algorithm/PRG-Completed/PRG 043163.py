def solution(str_s, str_t, lst_):
    if str_t not in lst_:
        return 0
    else:
        import heapq as hq
        INF_ = 100

        lst_.append(str_s)

        dct_ = dict()
        cnt_ = 0
        for str_a in lst_:
            dct_[str_a] = cnt_
            cnt_ += 1

        grp_ = [[] for _ in range(len(lst_))]
        for str_a in lst_:
            for str_b in lst_:
                if str_a != str_b:
                    cnt_ = 0
                    for chr_a, chr_b in zip(str_a, str_b):
                        if chr_a != chr_b:
                            cnt_ += 1
                            if cnt_ > 1:
                                break
                    if cnt_ == 1:
                        idx_a = dct_[str_a]
                        idx_b = dct_[str_b]
                        grp_[idx_a].append(idx_b)

        idx_s = dct_[str_s]
        idx_t = dct_[str_t]
        lst_iv = [False for _ in range(len(lst_))]
        lst_d = [INF_ for _ in range(len(lst_))]
        lst_d[idx_s] = 0

        hqu_ = [(0, idx_s)]
        while hqu_:
            dist_, idx_s = hq.heappop(hqu_)
            if not lst_iv[idx_s]:
                lst_iv[idx_s] = True
                for idx_e in grp_[idx_s]:
                    temp_ = dist_ + 1
                    if temp_ < lst_d[idx_e]:
                        lst_d[idx_e] = temp_
                        hq.heappush(hqu_, (temp_, idx_e))

        return lst_d[idx_t]


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
