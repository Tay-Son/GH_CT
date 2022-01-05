import sys

N_ = int(sys.stdin.readline())

lst_dp = [(0, 1)]
for idx_ in range(1, N_):
    lst_dp.append((sum(lst_dp[-1]), lst_dp[-1][0]))
print(sum(lst_dp[-1]))
exit()
