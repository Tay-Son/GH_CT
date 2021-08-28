import sys

N_, C_ = map(int, sys.stdin.readline().split())
dct_ = {}
for each_ in map(int, sys.stdin.readline().split()):
    if each_ in dct_:
        dct_[each_] += 1
    else:
        dct_[each_] = 1
lst_ = sorted(dct_.items(), key=lambda x: x[1], reverse=True)
lst_ans = []
for key_, value_ in lst_:
    lst_ans += [key_] * value_
print(' '.join(map(str, lst_ans)))

exit()
