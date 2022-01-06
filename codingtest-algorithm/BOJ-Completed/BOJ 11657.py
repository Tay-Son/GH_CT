import sys

INF_ = 10 ** 9

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(M_):
    a_, b_, w_ = map(int, sys.stdin.readline().split())
    grp_[a_].append((b_, w_))

lst_d = [INF_ for _ in range(N_ + 1)]
lst_d[1] = 0
is_ = False
for cnt_ in range(1, N_ + 1):
    for idx_ in range(1, N_ + 1):
        for idx_t, weight_ in grp_[idx_]:
            temp_ = weight_ + lst_d[idx_]
            if lst_d[idx_] != INF_ and temp_ < lst_d[idx_t]:
                lst_d[idx_t] = temp_
                if cnt_ == N_:
                    is_ = True

if is_:
    print(-1)
else:
    for idx_t in range(2, N_ + 1):
        print(lst_d[idx_t] if lst_d[idx_t] != INF_ else -1)

exit()
