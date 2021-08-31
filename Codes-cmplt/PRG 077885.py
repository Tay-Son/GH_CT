def solution(lst_number):
    lst_answer = []

    for number_ in lst_number:
        number_bin = list('0' + bin(number_)[2:])
        if number_bin[-1] == '0':
            lst_answer.append(number_ + 1)
        else:
            max_ = 0
            for ptr_ in range(2, len(number_bin)):
                if number_bin[ptr_] == '0':
                    max_ = max(max_, ptr_)
            number_bin[max_] = '1'
            number_bin[max_ + 1] = '0'
            lst_answer.append(int('0b' + ''.join(number_bin), 2))

    return lst_answer


print(solution([2, 7]))
