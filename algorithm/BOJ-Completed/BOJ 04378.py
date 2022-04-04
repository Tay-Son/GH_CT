import sys

str_a = " `1234567890- ASDFGHJKL; QWERTYUIOP[] ZXCVBNM,."
str_b = " 1234567890-= SDFGHJKL;\' WERTYUIOP[]\\ XCVBNM,./"

dct_ = {
    b_: a_ for a_, b_ in zip(str_a, str_b)
}
print(dct_)

str_ = sys.stdin.readline().rstrip()
while len(str_):
    ans_ = ''
    for each_ in str_:
        ans_ += dct_[each_]
    print(ans_)
    str_ = sys.stdin.readline().rstrip()
