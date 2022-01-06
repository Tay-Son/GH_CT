def solution(lst_str, str_target):
    import heapq as hq

    INF_ = 20001
    set_str = set(lst_str)

    lst_dp = [INF_ for _ in range(len(str_target) + 1)]
    lst_dp[0] = 0
    hqu_ = [(0, 0)]

    while hqu_:
        cnt_, ptr_s = hq.heappop(hqu_)
        cnt_ += 1
        for offset_ in range(1, 6):
            ptr_e = ptr_s + offset_
            if ptr_e <= len(str_target) and str_target[ptr_s:ptr_e] in set_str and lst_dp[ptr_e] > cnt_:
                lst_dp[ptr_e] = cnt_
                hq.heappush(hqu_, (cnt_, ptr_e))

    return lst_dp[-1] if lst_dp[-1] != INF_ else -1


print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
