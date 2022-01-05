def solution(lst_cookie):
    N_ = len(lst_cookie)
    max_ = 0
    max_sum_l = 0
    for ptr_m in range(1, N_):
        sum_l = 0
        max_sum_l += lst_cookie[ptr_m - 1]
        set_ = set()
        sum_r = 0
        ptr_r = ptr_m
        while sum_r < max_sum_l and ptr_r < N_:
            sum_r += lst_cookie[ptr_r]
            set_.add(sum_r)
            ptr_r += 1

        for ptr_l in range(ptr_m - 1, -1, -1):
            sum_l += lst_cookie[ptr_l]
            if sum_l > max_:
                if sum_l in set_:
                    max_ = sum_l

    return max_


print(solution([1, 1, 2, 3]))
