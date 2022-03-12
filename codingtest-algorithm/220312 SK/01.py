def solution(money_, lst_cost):
    lst_ = list(zip([1, 5, 10, 50, 100, 500], lst_cost))
    tot_ = 0
    for n_, c_ in sorted(lst_, key=lambda x: x[1] / x[0]):
        if money_:
            div_, money_ = divmod(money_, n_)
            tot_ += div_ * c_
        else:
            break
    return tot_


for money_, lst_cost in [
    (4578, [1, 4, 99, 35, 50, 1000]),
    (1999, [2, 11, 20, 100, 200, 600])
]:
    print(solution(money_, lst_cost))
