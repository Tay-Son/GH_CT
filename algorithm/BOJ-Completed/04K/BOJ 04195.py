import sys


def find_(dct_p, str_):
    temp_ = dct_p[str_]
    if temp_ != str_:
        temp_ = find_(dct_p, temp_)
        dct_p[str_] = temp_
    return temp_


def union_(dct_p, dct_c, str_a, str_b):
    p_a, p_b = find_(dct_p, str_a), find_(dct_p, str_b)
    if p_a != p_b:
        dct_p[p_a] = p_b
        dct_c[p_b] += dct_c[p_a]


for _ in range(int(sys.stdin.readline())):
    dct_p = dict()
    dct_c = dict()
    for _ in range(int(sys.stdin.readline())):
        str_a, str_b = sys.stdin.readline().split()
        if str_a not in dct_p:
            dct_p[str_a] = str_a
            dct_c[str_a] = 1
        if str_b not in dct_p:
            dct_p[str_b] = str_b
            dct_c[str_b] = 1

        union_(dct_p, dct_c, str_a, str_b)
        print(dct_c[find_(dct_p, str_a)])

exit()
