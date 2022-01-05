def solution(str_result):
    dct_mag = {'S': 1, 'D': 2, 'T': 3}

    lst_final_score = []
    score_ = 0
    temp_str = ''
    for each_ in str_result:
        print(each_)
        if each_ in set(list('0123456789')):
            temp_str += each_

        else:
            if len(temp_str):
                if score_:
                    lst_final_score.append(score_)
                score_ = int(temp_str)
                temp_str = ''

            if each_ in dct_mag:
                score_ **= dct_mag[each_]
            elif each_ == '*':
                if lst_final_score:
                    lst_final_score[-1] *= 2
                score_ *= 2
            elif each_ == '#':
                score_ *= -1
    lst_final_score.append(score_)

    return sum(lst_final_score)


print(solution("1T2D3D#"))
