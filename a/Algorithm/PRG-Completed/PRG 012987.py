def solution(lst_a, lst_b):
    lst_a.sort()
    lst_b.sort()
    ptr_a = 0
    score_ = 0
    for b_ in lst_b:
        if b_ > lst_a[ptr_a]:
            score_ += 1
            ptr_a += 1

    return score_


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
