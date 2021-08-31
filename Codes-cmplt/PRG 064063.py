def solution(K_, lst_room_number):
    import sys
    sys.setrecursionlimit(200009)
    dct_ = dict()

    def find_(idx_):
        if idx_ not in dct_:
            dct_[idx_] = idx_ + 1
            return idx_
        else:
            temp_ = find_(dct_[idx_])
            dct_[idx_] = temp_ + 1
            return temp_

    lst_answer = []
    for room_number in lst_room_number:
        lst_answer.append(find_(room_number))

    return lst_answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
exit()
