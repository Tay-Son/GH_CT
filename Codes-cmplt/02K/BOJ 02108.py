import sys
from collections import Counter

N = int(sys.stdin.readline())
lst_ = []
for _ in range(N):
    lst_.append(int(sys.stdin.readline()))

lst_.sort()

dct_ = Counter(lst_)
lst_dct = list(dct_)
max_ = max(Counter(lst_).values())
lst_temp = []
for each_ in lst_dct:
    if dct_[each_] == max_:
        lst_temp.append(each_)
lst_temp.sort()

print(round(sum(lst_) / N))
print(lst_[N // 2])
if len(lst_temp) > 1:
    print(lst_temp[1])
else:
    print(lst_temp[0])

print(max(lst_) - min(lst_))
