import heapq as hq


def solution(lst_people, l_):
    tot_ = 0
    hqu_ = []

    for people_ in sorted(lst_people, reverse=True):
        if hqu_ and hqu_[0][1] >= people_:
            _, val_ = hq.heappop(hqu_)
            hq.heappush(hqu_, (-val_ + people_, val_ - people_))
        else:
            hq.heappush(hqu_, (-l_ + people_, l_ - people_))
            tot_ += 1

    return tot_
