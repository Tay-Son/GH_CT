import sys
sys.setrecursionlimit(100009)

V_, E_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(V_ + 1)]
for _ in range(E_):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grp_[idx_a].append(idx_b)
    grp_[idx_b].append(idx_a)

cnt_ = 1
lst_cnt = [0 for _ in range(V_ + 1)]
set_ans = set()


def dfs_(idx_s, idx_p):
    global cnt_
    lst_cnt[idx_s] = cnt_
    min_ = cnt_
    cnt_ += 1

    for idx_e in grp_[idx_s]:
        if idx_e != idx_p:
            temp_ = lst_cnt[idx_e]
            if temp_:
                min_ = min(min_, temp_)
            else:

                temp_ = dfs_(idx_e, idx_s)
                if temp_ > lst_cnt[idx_s]:
                    set_ans.add((min(idx_s, idx_e), max(idx_s, idx_e)))
                min_ = min(min_, temp_)
    return min_


for idx_s in range(1, V_ + 1):
    if not lst_cnt[idx_s]:
        dfs_(idx_s, 0)

print(len(set_ans))
for each_ in sorted(list(set_ans)):
    print(' '.join(map(str, each_)))

exit()
