def solution(str_):
    dct_ = {'(': ')', '[': ']', '{': '}'}
    tot_ = 0
    for ptr_s in range(len(str_)):
        stk_ = []
        is_ = True
        for offset_ in range(len(str_)):
            idx_ = (ptr_s + offset_) % len(str_)
            target_chr = str_[idx_]
            if target_chr in dct_:
                stk_.append(target_chr)
            elif stk_ and dct_[stk_[-1]] == target_chr:
                stk_.pop()
            else:
                is_ = False
                break
        if stk_:
            is_ = False
        tot_ += int(is_)

    return tot_


print(solution("}]()[{"))
