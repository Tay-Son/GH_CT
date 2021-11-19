import sys
from itertools import permutations as pm

N_, M_ = map(int, sys.stdin.readline().split())
set_ = set()
for lst_pm in pm(map(int, sys.stdin.readline().split()), M_):
    tup_pm = tuple(lst_pm)
    if tup_pm not in set_:
        set_.add(tup_pm)

for each_tup in sorted(set_):
    print(' '.join(map(str, each_tup)))

exit()
