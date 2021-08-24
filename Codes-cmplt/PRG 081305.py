def rec_(thres_, idx_p, lst_tot, lst_num, lst_link):
    if lst_tot[idx_p] == -1:
        global rem_slice
        tot_ = lst_num[idx_p]
        lst_temp = []
        for idx_c in lst_link[idx_p]:
            if idx_c != -1:
                lst_temp.append(rec_(thres_, idx_c, lst_tot, lst_num, lst_link))

        if len(lst_temp) == 0:
            pass
        elif len(lst_temp) == 1:
            if tot_ + lst_temp[0] > thres_:
                rem_slice -= 1
            else:
                tot_ += lst_temp[0]
        else:
            if tot_ + sum(lst_temp) <= thres_:
                tot_ += sum(lst_temp)
            elif tot_ + min(lst_temp) <= thres_:
                tot_ += min(lst_temp)
                rem_slice -= 1
            else:
                rem_slice -= 2

        lst_tot[idx_p] = tot_

    return lst_tot[idx_p]


def solution(K_, lst_num, lst_link):
    import sys
    sys.setrecursionlimit(10009)

    ptr_s = max(lst_num)
    ptr_e = 100000000
    while ptr_s < ptr_e:
        ptr_c = (ptr_s + ptr_e) // 2

        global rem_slice
        rem_slice = K_ - 1
        lst_tot = [-1 for _ in range(len(lst_num))]
        for idx_p in range(len(lst_num)):
            rec_(ptr_c, idx_p, lst_tot, lst_num, lst_link)
        print(ptr_s, ptr_e, ptr_c, lst_tot, rem_slice)

        if rem_slice >= 0 and max(lst_tot) <= ptr_c:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1

    return ptr_s


print(solution(3,
               [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
               [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1],
                [-1, -1]]))
