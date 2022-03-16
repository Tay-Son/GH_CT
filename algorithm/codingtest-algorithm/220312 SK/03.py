DIV_ = 10000019


def comb_(a_, b_):
    b_ = min(b_, a_ - b_)
    nume_ = 1
    deno_ = 1
    for num_ in range(b_):
        deno_ *= (num_ + 1)
        nume_ *= (a_ - num_)
    return nume_ // deno_


def solution(R_, C_, lst_d):
    tot_ = 0
    for r_, c_ in lst_d:
        r_c, c_c = R_ - r_, C_ - c_

        tot_ += comb_(r_ + c_ - 1, r_ - 1) * comb_(r_c + c_c + 1, r_c)
        tot_ %= DIV_

        tot_ += comb_(r_ + c_ - 1, c_ - 1) * comb_(r_c + c_c + 1, c_c)
        tot_ %= DIV_

    return tot_


for R_, C_, lst_d in [
    (2, 2, [[1, 1], [2, 2]]),
    (51, 37, [[17, 19]])
]:
    print(solution(R_, C_, lst_d))
