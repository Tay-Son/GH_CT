def solution(lst_):
    lst_.sort(reverse=True)

    ptr_ = 0
    for val_c in range(lst_[0], -1, -1):
        while ptr_ < len(lst_) and lst_[ptr_] >= val_c:
            ptr_ += 1
        if ptr_ + 1 > val_c:
            break

    return val_c


print(solution([3, 0, 6, 1, 5]))
