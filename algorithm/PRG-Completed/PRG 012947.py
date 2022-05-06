def solution(x_):
    c_ = 0
    x_c = x_
    while x_c > 9:
        x_c, mod_ = divmod(x_c, 10)
        c_ += mod_
    c_ += x_c
    return not x_ % c_
