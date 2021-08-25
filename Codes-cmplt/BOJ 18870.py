import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_sub = sorted(lst_)
cnt_ = 0
past_ = lst_sub[0]
dct_ = {}
for each_ in lst_sub:
    if each_ != past_:
        past_ = each_
        cnt_ += 1
    dct_[each_] = cnt_
print(' '.join(map(lambda x: str(dct_[x]), lst_)))

exit()
