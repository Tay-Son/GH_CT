import sys
from itertools import combinations as cb

T_ = int(sys.stdin.readline())
N_ = int(sys.stdin.readline())
lst_n = list(map(int, sys.stdin.readline().split()))
M_ = int(sys.stdin.readline())
lst_m = list(map(int, sys.stdin.readline().split()))

dct_n = dict()
lst_nt = [0]
tot_ = 0
for each_ in lst_n:
    tot_ += each_
    lst_nt.append(tot_)
for a_, b_ in cb(lst_nt, 2):
    temp_ = b_ - a_
    if temp_ not in dct_n:
        dct_n[temp_] = 1
    else:
        dct_n[temp_] += 1

dct_m = dict()
lst_mt = [0]
tot_ = 0
for each_ in lst_m:
    tot_ += each_
    lst_mt.append(tot_)
for a_, b_ in cb(lst_mt, 2):
    temp_ = b_ - a_
    if temp_ not in dct_m:
        dct_m[temp_] = 1
    else:
        dct_m[temp_] += 1

tot_ = 0
for key_, value_ in dct_n.items():
    temp_ = T_ - key_
    if temp_ in dct_m:
        tot_ += dct_m[temp_] * value_

print(tot_)

exit()
