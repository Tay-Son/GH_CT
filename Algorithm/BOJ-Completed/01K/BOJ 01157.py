import sys

dct_ = dict()
for each_chr in sys.stdin.readline().upper():
    if 'A' <= each_chr <= 'Z':
        if each_chr not in dct_:
            dct_[each_chr] = 1
        else:
            dct_[each_chr] += 1

if dct_:
    lst_ = sorted(dct_.items(), key=lambda x: x[1], reverse=True)
    if len(lst_) > 1 and lst_[0][1] == lst_[1][1]:
        print('?')
    else:
        print(lst_[0][0])
else:
    print('?')

exit()
