def solution(N_, A_, B_):
    A_ -= 1
    B_ -= 1
    cnt_ = 0
    while A_ != B_:
        cnt_ += 1
        A_ //= 2
        B_ //= 2
    return cnt_


print(solution(8, 4, 7))
