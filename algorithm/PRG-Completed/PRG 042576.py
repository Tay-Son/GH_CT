def solution(participant, completion):
    dct_ = dict()
    for each_ in participant:
        if each_ not in dct_:
            dct_[each_] = 1
        else:
            dct_[each_] += 1

    for each_ in completion:
        if dct_[each_] == 1:
            dct_.pop(each_)
        else:
            dct_[each_] -= 1
    return list(dct_.keys())[0]