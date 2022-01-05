import sys
from itertools import permutations as pm

N_, M_ = map(int, sys.stdin.readline().split())
lst_ = list(map(int,sys.stdin.readline().split()))
lst_.sort()

for lst_pm in pm(lst_, M_):
    print(' '.join(map(str,lst_pm)))

exit()
