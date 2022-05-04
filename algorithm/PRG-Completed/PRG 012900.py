DIV_ = 1000000007


def solution(N_):
    lst_ = [1, 1, 2]
    for _ in range(2, N_ + 1):
        lst_.append((lst_[-1] + 2 * lst_[-2]) % DIV_)
    print(lst_)
    return lst_[-1]
