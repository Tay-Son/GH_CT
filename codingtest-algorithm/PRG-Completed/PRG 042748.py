def solution(lst_, lst_command):
    lst_answer = []

    for each_command in lst_command:
        start_, end_, target_ = each_command
        lst_sub = sorted(lst_[start_ - 1:end_])
        lst_answer.append(lst_sub[target_ - 1])

    return lst_answer