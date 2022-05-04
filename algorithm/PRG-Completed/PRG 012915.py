def solution(lst_str, N_):
    lst_str.sort()
    lst_str.sort(key=lambda x: x[N_])
    return lst_str
