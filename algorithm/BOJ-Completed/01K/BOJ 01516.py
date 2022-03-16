import sys

N = int(sys.stdin.readline())
lst_t = [0]
lst_o = [[]]
for _ in range(N):
    lst_input = list(map(int, sys.stdin.readline().split()))
    lst_t.append(lst_input[0])
    lst_o.append(lst_input[1:-1])

lst_c = [0 for _ in range(N + 1)]


def func(idx_):
    if lst_c[idx_] != 0:
        return lst_c[idx_]
    else:
        max_ = 0
        for each_ in lst_o[idx_]:
            max_ = max(max_, func(each_))
        lst_c[idx_] = max_ + lst_t[idx_]
        return lst_c[idx_]


for idx_ in range(1, N + 1):
    print(func(idx_))

exit()