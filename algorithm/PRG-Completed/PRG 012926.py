def solution(str_, N_):
    str_ans = ''
    for chr_ in str_:
        if 'a' <= chr_ <= 'z':
            str_ans += chr(((ord(chr_) + N_ - ord('a')) % 26) + ord('a'))
        elif 'A' <= chr_ <= 'Z':
            str_ans += chr(((ord(chr_) + N_ - ord('A')) % 26) + ord('A'))
        else:
            str_ans += chr_

    return str_ans
