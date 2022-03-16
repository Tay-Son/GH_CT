def solution(str_number, K_):
    stk_ = []
    for chr_ in str_number:
        while K_ and stk_ and stk_[-1] < chr_:
            stk_.pop()
            K_ -= 1
        stk_.append(chr_)
    while K_:
        stk_.pop()
        K_ -= 1

    return ''.join(stk_)
