import sys

sys.setrecursionlimit(10 ** 5)
V_, E_ = map(int, sys.stdin.readline().split())

grp_ = [set() for _ in range(V_ + 1)]
for _ in range(E_):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grp_[idx_a].add(idx_b)
    grp_[idx_b].add(idx_a)

lst_cnt = [-1 for _ in range(V_ + 1)]
set_ans = set()
cnt_ = 1


def rec_(idx_, idx_departure):
    global cnt_
    lst_cnt[idx_] = cnt_
    min_ = cnt_
    cnt_ += 1

    C_ = 0
    for idx_t in grp_[idx_]:
        temp_ = lst_cnt[idx_t]
        if temp_ != -1:
            min_ = min(min_, temp_)
        else:
            C_ += 1
            temp_ = rec_(idx_t, idx_departure)
            if idx_ != idx_departure and temp_ >= lst_cnt[idx_]:
                set_ans.add(idx_)
            min_ = min(min_, temp_)

    if idx_ == idx_departure and C_ > 1:
        set_ans.add(idx_)
    return min_


for idx_ in range(1, V_ + 1):
    if lst_cnt[idx_] == -1:
        rec_(idx_, idx_)

set_ans2 = set()
for idx_s in set_ans:
    for idx_e in grp_[idx_s]:
        if idx_e in set_ans:
            set_ans2.add((min(idx_s, idx_e), max(idx_s, idx_e)))
print(len(set_ans2))
for each_ in sorted(list(set_ans2)):
    print(' '.join(map(str, each_)))

exit()
