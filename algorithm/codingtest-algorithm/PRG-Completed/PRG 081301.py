def solution(str_):
    dct_ = {str_: str(idx_) for str_, idx_ in
            zip(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], range(10))}

    str_answer = ''
    ptr_ = 0
    while ptr_ < len(str_):
        chr_ = str_[ptr_]
        if '0' <= chr_ <= '9':
            str_answer += chr_
            ptr_ += 1
        else:
            for key_ in dct_.keys():
                ptr_temp = ptr_ + len(key_)
                if ptr_temp <= len(str_) and \
                        str_[ptr_:ptr_temp] == key_:
                    str_answer += dct_[key_]
                    break
            ptr_ = ptr_temp
    return int(str_answer)
