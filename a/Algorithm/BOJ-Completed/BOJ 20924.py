import sys
sys.setrecursionlimit(200001)

N_, R_ = map(int, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_ + 1)]
lst_is_visited = [False for _ in range(N_ + 1)]

for _ in range(N_ - 1):
    a_, b_, d_ = map(int, sys.stdin.readline().split())
    grp_[a_].append((b_, d_))
    grp_[b_].append((a_, d_))

br_ = 0
pn_ = 0


def rec_(curr_, tot_):
    global pn_
    lst_is_visited[curr_] = True
    count_ = 0
    for suc_, depth_ in grp_[curr_]:
        if lst_is_visited[suc_] == False:
            rec_(suc_, tot_ + depth_)
            count_ += 1
    if not count_:
        pn_ = max(pn_, tot_)


while True:
    lst_is_visited[R_] = True
    count_ = 0
    for suc_, depth_ in grp_[R_]:
        if lst_is_visited[suc_] == False:
            count_ += 1
            temp_suc = suc_
            temp_depth = depth_

    if count_ == 1:
        R_ = temp_suc
        br_ += temp_depth
    elif count_ > 1:
        rec_(R_, 0)
        break
    elif count_ == 0:
        break

print(br_, pn_)

exit()