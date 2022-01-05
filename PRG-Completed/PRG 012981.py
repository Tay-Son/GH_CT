def solution(N_, lst_word):
    lst_answer = [0, 0]

    set_ = set()

    cycle_ = 0
    ptr_ = 0
    is_run = True
    is_first = True

    while is_run:
        cycle_ += 1
        for idx_ in range(N_):
            if ptr_ < len(lst_word):
                if lst_word[ptr_] not in set_:
                    if is_first:
                        is_first = False
                    else:
                        if lst_word[ptr_][0] != last_chr:
                            lst_answer = [idx_ + 1, cycle_]
                            is_run = False
                            break
                    set_.add(lst_word[ptr_])
                    last_chr = lst_word[ptr_][-1]
                else:
                    lst_answer = [idx_ + 1, cycle_]
                    is_run = False
                    break
            else:
                is_run = False
                break
            ptr_ += 1

    return lst_answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
