def solution(str_a, str_b):
    dct_a = dict()
    dct_b = dict()
    for chr_1, chr_2 in zip(str_a[:-1], str_a[1:]):
        if ord('A') <= ord(chr_1.upper()) <= ord('Z') and ord('A') <= ord(chr_2.upper()) <= ord('Z'):
            str_temp = (chr_1 + chr_2).upper()
            if str_temp not in dct_a:
                dct_a[str_temp] = 1
            else:
                dct_a[str_temp] += 1

    for chr_1, chr_2 in zip(str_b[:-1], str_b[1:]):
        if ord('A') <= ord(chr_1.upper()) <= ord('Z') and ord('A') <= ord(chr_2.upper()) <= ord('Z'):
            str_temp = (chr_1 + chr_2).upper()
            if str_temp not in dct_b:
                dct_b[str_temp] = 1
            else:
                dct_b[str_temp] += 1

    nume_ = 0
    deno_ = 0

    for key_, value_ in dct_a.items():
        if key_ in dct_b:
            nume_ += min(value_, dct_b[key_])
            deno_ += max(value_, dct_b[key_])
        else:
            deno_ += value_
    for key_, value_ in dct_b.items():
        if key_ not in dct_a:
            deno_ += value_

    if deno_:
        return int(nume_ / deno_ * 65536)
    else:
        return 65536


print(solution("aa1+aa2", "AAAA12"))
