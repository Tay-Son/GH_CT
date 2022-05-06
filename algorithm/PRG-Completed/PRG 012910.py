def solution(lst_num, div_):
    lst_ = []
    for num_ in lst_num:
        if not num_ % div_:
            lst_.append(num_)

    if not lst_:
        lst_.append(-1)

    return sorted(lst_)
