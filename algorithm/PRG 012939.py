def solution(str_):
    lst_ = list(map(int, str_.split()))

    return ' '.join(map(str, [min(lst_), max(lst_)]))
