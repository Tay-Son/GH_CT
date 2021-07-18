import sys

sys.setrecursionlimit(10 ** 5)
V_, E_ = map(int, sys.stdin.readline().split())

grp_ = [[] for _ in range(V_ + 1)]
for _ in range(E_):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grp_[idx_a].append(idx_b)
    grp_[idx_b].append(idx_a)

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

print(len(set_ans))
print(' '.join(map(str, sorted(list(set_ans)))))

exit()
