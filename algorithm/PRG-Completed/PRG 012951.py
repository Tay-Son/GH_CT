def solution(str_):
    str_o = ''
    is_ = True
    for chr_ in str_:
        if chr_.isupper():
            chr_ = chr_.lower()

        if chr_ == ' ':
            is_ = True
        else:
            if is_ and chr_.islower():
                chr_ = chr_.upper()
            is_ = False
        str_o += chr_
    return str_o


print(solution('aBc  5abc'))
