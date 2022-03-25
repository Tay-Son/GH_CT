from bisect import bisect_right


def solution(lst_food, k_):
    lst_food_sorted = sorted(lst_food)
    lst_food_sum = [0]
    N_ = len(lst_food)
    sum_ = 0
    for food_sorted in lst_food_sorted:
        sum_ += food_sorted
        lst_food_sum.append(sum_)

    ptr_s = 0
    ptr_e = 100000000

    max_ = 0
    max_tot = 0
    while ptr_s + 1 < ptr_e:
        ptr_c = (ptr_s + ptr_e) // 2

        tot_ = 0

        v_ = bisect_right(lst_food_sorted, ptr_c)

        tot_ = lst_food_sum[v_] + (N_ - v_) * ptr_c

        # for each_food in lst_food:
        #     tot_ += min(ptr_c, each_food)
        if tot_ <= k_:
            if ptr_c > max_:
                max_ = ptr_c
                max_tot = tot_
            ptr_s = ptr_c
        else:
            ptr_e = ptr_c

    k_ -= max_tot - 1
    idx = 0
    cnt_ = 0
    answer = -1
    for each_food in lst_food:
        idx += 1
        if each_food > max_:
            cnt_ += 1
            if cnt_ == k_:
                answer = idx
                break

    return answer
