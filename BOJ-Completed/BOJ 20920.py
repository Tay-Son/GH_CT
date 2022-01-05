import sys

N_, M_ = map(int, sys.stdin.readline().split())

dct_ = dict()
for _ in range(N_):
    str_ = sys.stdin.readline().strip()
    temp_ = len(str_)
    if temp_ >= M_:
        if str_ in dct_:
            dct_[str_] += 1
        else:
            dct_[str_] = 1
lst_ = sorted(dct_.items(), key=lambda x: x[0])
lst_.sort(key=lambda x: len(x[0]), reverse=True)
lst_.sort(key=lambda x: x[1], reverse=True)

for str_, count_ in lst_:
    print(str_)

exit()