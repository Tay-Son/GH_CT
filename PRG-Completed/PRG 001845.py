def solution(lst_num):
    N_ = len(lst_num)
    set_ = set(lst_num)
    return min(len(set_), N_ // 2)


print(solution([3, 3, 3, 2, 2, 4]))
