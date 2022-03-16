import sys
sys.setrecursionlimit(10**4)


def depth_(idx_, lst_depth, lst_parent):
    if lst_depth[idx_] == -1:
        idx_parent = lst_parent[idx_]
        if idx_parent == 0:
            lst_depth[idx_] = 0
        else:
            lst_depth[idx_] = depth_(idx_parent, lst_depth, lst_parent) + 1
    return lst_depth[idx_]


for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    lst_parent = [0 for _ in range(N_ + 1)]
    for _ in range(N_ - 1):
        val_a, val_b = map(int, sys.stdin.readline().split())
        lst_parent[val_b] = val_a

    lst_depth = [-1 for _ in range(N_ + 1)]
    for idx_ in range(1, N_ + 1):
        lst_depth[idx_] = depth_(idx_, lst_depth, lst_parent)

    val_a, val_b = map(int, sys.stdin.readline().split())

    while lst_depth[val_a] > lst_depth[val_b]:
        val_a = lst_parent[val_a]
    while lst_depth[val_a] < lst_depth[val_b]:
        val_b = lst_parent[val_b]
    while val_a != val_b:
        val_a = lst_parent[val_a]
        val_b = lst_parent[val_b]
    print(val_a)

exit()