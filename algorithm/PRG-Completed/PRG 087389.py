def solution(N_):
    N_ -= 1
    C_ = 2
    while N_ % C_ and C_ <= int(N_ ** .5) + 1:
        C_ += 1
    if N_ % C_:
        return N_
    else:
        return C_
