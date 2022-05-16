import sys

N_ = int(sys.stdin.readline())
lst_tre = [1]
for _ in range(1, N_):
    lst_temp = [2 * val_ + (idx_ % 2) for idx_, val_ in enumerate(lst_tre)]
    lst_temp += [1]
    lst_temp += [2 * val_ + ((idx_ + 1) % 2) for idx_, val_ in enumerate(lst_tre)]
    lst_tre = lst_temp
print(lst_tre)

lst_ans = []


def pre_order(idx_, depth_):
    lst_ans.append(lst_tre[idx_])
    if depth_:
        pre_order(idx_ - 2 ** (depth_ - 1), depth_ - 1)
        pre_order(idx_ + 2 ** (depth_ - 1), depth_ - 1)


pre_order((2 ** (N_ - 1) - 1), N_ - 1)

print(' '.join(map(str, lst_ans)))

exit()
