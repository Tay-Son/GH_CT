def solution(v_gold, v_silver, lst_gold, lst_silver, lst_weight, lst_time):
    N_ = len(lst_gold)
    ptr_s = 0
    ptr_e = 1000000000

    lst_idx = list(range(N_))
    lst_idx.sort(key=lambda x: lst_silver[x])
    lst_idx.sort(key=lambda x: lst_gold[x])
    print(lst_idx)
    while ptr_s < ptr_e:
        ptr_c = (ptr_s + ptr_e) // 2

        tot_gold = v_gold
        tot_silver = v_silver

        for idx_ in lst_idx:
            weight_ = lst_weight[idx_]
            time_ = lst_time[idx_]
            cnt_ = ptr_c // time_ + 1
            cnt_ //= 2
            max_weight = weight_ * cnt_


            if tot_gold:
                temp_val = min(lst_gold[idx_], tot_gold, max_weight)
                tot_gold -= temp_val
                max_weight -= temp_val
            if tot_silver:
                temp_val = min(lst_silver[idx_], tot_silver, max_weight)
                tot_silver -= temp_val

        if not (tot_gold or tot_silver):
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1

    return ptr_s


print(solution(90,
               500,
               [70, 70, 0],
               [0, 0, 500],
               [100, 100, 2],
               [4, 8, 1]))
