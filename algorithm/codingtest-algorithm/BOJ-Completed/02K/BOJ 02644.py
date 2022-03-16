import sys

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
idx_a, idx_b = map(int, sys.stdin.readline().split())

for _ in range(int(sys.stdin.readline())):
    temp_a, temp_b = map(int, sys.stdin.readline().split())
    grp_[temp_a].append(temp_b)
    grp_[temp_b].append(temp_a)

ans_ = -1


def func_(idx_curr, idx_dprt, depth_):
    global ans_
    if idx_curr == idx_b:
        ans_ = depth_
    else:
        depth_ += 1
        for idx_target in grp_[idx_curr]:
            if idx_target != idx_dprt:
                func_(idx_target, idx_curr, depth_)


func_(idx_a, 0, 0)

print(ans_)

exit()