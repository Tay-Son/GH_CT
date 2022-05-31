import sys

N_ = int(sys.stdin.readline())
lst_a = list(map(int, sys.stdin.readline().split()))
lst_b = [val_[0] for val_ in sorted([(idx_, val_) for idx_, val_ in enumerate(lst_a)], key=lambda x: x[1])]

lst_p = [0 for _ in range(N_)]
for idx_, val_ in enumerate(lst_b):
    lst_p[val_] = idx_

print(' '.join(map(str, lst_p)))

exit()
