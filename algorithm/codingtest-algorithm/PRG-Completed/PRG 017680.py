def solution(siz_cache, lst_city):
    from collections import deque

    tot_ = 0
    deq_cache = deque()
    for city, idx_ in zip(lst_city, range(len(lst_city))):
        city = city.upper()
        is_ = False
        for cnt_ in range(1, min(len(deq_cache), siz_cache)+1):
            if deq_cache[-cnt_] == city:
                print(cnt_)
                is_ = True
                del (deq_cache[-cnt_])
                break
        if is_:
            tot_ += 1
        else:
            tot_ += 5
        deq_cache.append(city)
        print(city, idx_, tot_)
        print(deq_cache)
        print()
    return tot_


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
