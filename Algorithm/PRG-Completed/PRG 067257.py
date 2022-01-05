def solution(str_expression):
    from itertools import permutations as pm
    set_o = {'+', '-', '*'}

    lst_ = []
    str_temp = ''
    for each_chr in str_expression:
        if each_chr in set_o:
            lst_.append(int(str_temp))
            lst_.append(each_chr)
            str_temp = ''
        else:
            str_temp += each_chr
    lst_.append(int(str_temp))

    max_ = 0
    for pm_ in pm(set_o):
        lst_copy = lst_.copy()
        for each_o in pm_:
            ptr_ = 1
            print(lst_copy)
            while ptr_ < len(lst_copy)-1:
                o_ = lst_copy[ptr_]
                if o_ == each_o:
                    num_ = lst_copy[ptr_ + 1]

                    del (lst_copy[ptr_])
                    del (lst_copy[ptr_])

                    if o_ == '*':
                        lst_copy[ptr_ - 1] *= num_
                    elif o_ == '-':
                        lst_copy[ptr_ - 1] -= num_
                    else:
                        lst_copy[ptr_ - 1] += num_
                else:
                    ptr_ += 2
            print(lst_copy)
        max_ = max(max_, abs(lst_copy[0]))
        print()
    return max_


print(solution("100-200*300-500+20"))
