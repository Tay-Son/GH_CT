from itertools import permutations as pm


def solution(lst_number):
    set_ = set()

    for num_ in range(1, len(lst_number) + 1):
        for pm_ in pm(lst_number, num_):
            set_.add(int(''.join(pm_)))

    for each_ in [0, 1]:
        if each_ in set_:
            set_.remove(each_)

    cnt_ = 0
    for each_ in set_:
        print(each_)
        for num_ in range(2, int(each_ ** .5) + 1):
            if not each_ % num_:
                break
        else:

            cnt_ += 1

    return cnt_


print(solution("17"))
