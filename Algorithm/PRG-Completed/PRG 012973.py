def solution(str_):
    stk_ = []
    for each_chr in str_:
        if stk_ and each_chr == stk_[-1]:
            stk_.pop()
        else:
            stk_.append(each_chr)

    return int(not stk_)

