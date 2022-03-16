def solution(clothes):
    dct_ = dict()
    for each_cloth in clothes:
        target_ = each_cloth[1]
        if target_ not in dct_:
            dct_[target_] = 1
        else:
            dct_[target_] += 1
    answer = 1
    for each_ in dct_.values():
        answer *= (each_ + 1)

    return answer - 1