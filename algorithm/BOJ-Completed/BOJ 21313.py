import sys

N_ = int(sys.stdin.readline())
lst_ = [1 + idx_ % 2 for idx_ in range(N_ - 1)]
if N_ % 2:
    lst_.append(3)
else:
    lst_.append(2)
print(' '.join(map(str, lst_)))
exit()
