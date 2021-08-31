import sys

dct_ = dict()
for _ in range(int(sys.stdin.readline())):
    str_input = sys.stdin.readline().rstrip()
    if str_input not in dct_:
        dct_[str_input] = 1
    else:
        dct_[str_input] += 1
lst_ = sorted(dct_.items())
print(sorted(lst_, key=lambda x: x[1], reverse=True)[0][0])

exit()
