def solution(lst_scoville, K_):
    import heapq as hq

    hqu_ = []
    for each_scoville in lst_scoville:
        hq.heappush(hqu_, each_scoville)

    cnt_ = 0
    while len(hqu_) > 1 and hqu_[0] < K_:
        temp_a = hq.heappop(hqu_)
        temp_b = hq.heappop(hqu_)
        hq.heappush(hqu_, temp_a + 2 * temp_b)
        cnt_ += 1

    if hqu_[0] < K_:
        cnt_ = -1

    return cnt_