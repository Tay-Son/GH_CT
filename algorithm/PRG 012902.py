DIV_ = 1000000007


def solution(N_):
    lst_ = [1, 0, 3, 0, 11]
    for _ in range(4, N_):
        lst_.append((3 * lst_[-2] + 2 * lst_[-4]) % DIV_)
    return lst_[-1]
