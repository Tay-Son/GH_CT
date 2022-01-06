def solution(str_):
    lst_ = [0, 0]
    while len(str_) > 1:
        cnt_ = str_.count('1')
        lst_[1] += len(str_) - cnt_
        str_ = bin(cnt_)[2:]
        lst_[0] += 1

    return lst_


print(solution("110010101001"))
