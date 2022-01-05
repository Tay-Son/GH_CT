import sys
import math

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
B_, C_ = map(int, sys.stdin.readline().split())

tot_ = N_
for each_ in lst_:
    each_ -= B_
    tot_ += max(0, math.ceil(each_ / C_))
print(tot_)

exit()
