import sys
import bisect

N_, M_, K_ = map(int, sys.stdin.readline().split())

lst_blue = sorted([int(x) - 1 for x in sys.stdin.readline().split()])
lst_sub = [idx_ for idx_ in range(N_)]


def find_(idx_):
    temp_ = lst_sub[idx_]
    if temp_ != idx_:
        temp_ = find_(temp_)
        lst_sub[idx_] = temp_
    return temp_


def use_(idx_):
    idx_temp = find_(idx_)
    lst_sub[idx_temp] = find_(idx_temp + 1)
    return idx_temp


for red_ in [int(x) - 1 for x in sys.stdin.readline().split()]:
    print(lst_blue[use_(bisect.bisect(lst_blue, red_))] + 1)

exit()
