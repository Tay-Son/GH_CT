def solution(L_, R_):
    lst_ = [2 for _ in range(R_ + 1)]
    lst_[1] = 1

    for cnt_ in range(2, R_ // 2 + 1):
        idx_ = cnt_ * 2
        while idx_ <= R_:
            lst_[idx_] += 1
            idx_ += cnt_

    print(lst_)
    tot_ = 0
    for idx_ in range(L_, R_ + 1):
        tot_ += -idx_ if lst_[idx_] % 2 else idx_

    return tot_

print(solution(24,27))