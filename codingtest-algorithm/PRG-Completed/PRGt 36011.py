def solution(lst_A, lst_B):
    lst_B.sort()
    ptr_b = 0
    cnt_ = 0

    for a_ in sorted(lst_A):
        while ptr_b < len(lst_B) and lst_B[ptr_b] <= a_:
            ptr_b += 1
        if ptr_b == len(lst_B):
            break
        elif lst_B[ptr_b] > a_:
            cnt_ += 1
            ptr_b += 1

    return cnt_
