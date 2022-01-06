import sys
from itertools import combinations as cb

val_L, val_C = map(int, sys.stdin.readline().split())
lst_cands = sys.stdin.readline().split()

lst_cons = []
lst_vowl = []

for cand in lst_cands:
    if cand in ['a', 'e', 'i', 'o', 'u']:
        lst_cons.append(cand)
    else:
        lst_vowl.append(cand)

lst_answer = []
for cnt_cons in range(1, min(val_L - 2, len(lst_vowl)) + 1):
    for cb_cons in cb(lst_cons, cnt_cons):
        for cb_vowl in cb(lst_vowl, val_L - cnt_cons):
            lst_answer.append(''.join(sorted((list(cb_cons) + list(cb_vowl)))))
lst_answer.sort()
for each_ in lst_answer:
    print(each_)