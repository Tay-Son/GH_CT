import sys

INF_ = 10 ** 9

for _ in range(int(sys.stdin.readline())):
    N_, M_, W_ = map(int, sys.stdin.readline().split())
    grp_ = [[] for _ in range(N_ + 1)]

    for _ in range(M_):
        S_, E_, T_ = map(int, sys.stdin.readline().split())
        grp_[S_].append((E_, T_))
        grp_[E_].append((S_, T_))

    for _ in range(W_):
        S_, E_, T_ = map(int, sys.stdin.readline().split())
        grp_[S_].append((E_, -T_))

    lst_distance = [INF_ for _ in range(N_ + 1)]
    lst_p = [-1 for _ in range(N_ + 1)]

    is_ = False

    for cnt_ in range(1, N_ + 1):
        for idx_ in range(1, N_ + 1):
            for idx_t, weight_ in grp_[idx_]:
                temp_ = weight_ + lst_distance[idx_]
                if temp_ < lst_distance[idx_t]:
                    lst_distance[idx_t] = temp_
                    if cnt_ == N_:
                        is_ = True
    if is_:
        print('YES')
    else:
        print('NO')

exit()
