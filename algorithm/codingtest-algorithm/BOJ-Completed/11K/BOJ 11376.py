import sys

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(N_ + 1)]
lst_d = [0 for _ in range(M_ + 1)]

for _ in range(M_):
    idx_u, idx_n = map(int, sys.stdin.readline().split())
    grp_[idx_u].append(idx_n)


def func_(idx_u):
    if lst_iv[idx_u]:
        return False
    else:
        lst_iv[idx_u] = True
        for idx_n in grp_[idx_u]:
            if lst_d[idx_n] == 0 or func_(lst_d[idx_n]):
                lst_d[idx_n] = idx_u
                return True
        return False


answer_ = 0
for idx_u in range(1, N_ + 1):
    lst_iv = [False for _ in range(N_ + 1)]
    answer_ += int(func_(idx_u))
print(answer_)

exit()
