import sys

N_ = int(sys.stdin.readline())
lst_ant = [0]
for _ in range(N_):
    lst_ant.append(int(sys.stdin.readline()))

grp_ = [[] for _ in range(N_ + 1)]
for _ in range(N_ - 1):
    idx_a, idx_b, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_a].append((idx_b, weight_))
    grp_[idx_b].append((idx_a, weight_))

lst_p = [[0, 0] for _ in range(N_ + 1)]
lst_p[1] = [-1, 0]


def func_(idx_s):
    for idx_e, weight_ in grp_[idx_s]:
        if lst_p[idx_e][0] == 0:
            lst_p[idx_e][0] = idx_s
            lst_p[idx_e][1] = weight_
            func_(idx_e)


func_(1)

for idx_ in range(1, N_ + 1):
    idx_curr = idx_
    while lst_p[idx_curr][0] != -1 and lst_ant[idx_] >= lst_p[idx_curr][1]:
        lst_ant[idx_] -= lst_p[idx_curr][1]
        idx_curr = lst_p[idx_curr][0]
    print(idx_curr)

print(lst_p)
exit()

import sys

N_ = int(sys.stdin.readline())
lst_n = [0]
for _ in range(N_):
    lst_n.append(int(sys.stdin.readline()))
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(N_ - 1):
    A_, B_, W_ = map(int, sys.stdin.readline().split())
    grp_[A_].append((B_, W_))
    grp_[B_].append((A_, W_))

stk_ = [(1, 0)]
lst_visited = [False for _ in range(N_ + 1)]
lst_d = [1 for _ in range(N_ + 1)]


def func(idx_):
    lst_visited[idx_] = True

    for T_, W_ in grp_[idx_]:
        if not lst_visited[T_]:
            stk_.append((T_, W_))

            temp_ = lst_n[T_]
            for idx_ in range(len(stk_) - 1, -1, -1):
                if temp_ >= stk_[idx_][1]:
                    temp_ -= stk_[idx_][1]
                else:
                    break
            lst_d[T_] = stk_[idx_][0]
            func(T_)

            stk_.pop()


func(1)
for idx_ in range(1, N_ + 1):
    print(lst_d[idx_])
exit()
